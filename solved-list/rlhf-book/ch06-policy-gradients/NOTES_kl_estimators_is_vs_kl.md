# Notes: KL estimator fix, then IS (k1 / k2 / k3)

Companion to the Chapter 6 GRPO KL-estimator comparison
([REPORT.md](REPORT.md)).

I wrote this after the book authors pointed out that the KL estimators in
`policy_gradients/loss.py` were wrong
([issue #489](https://github.com/natolambert/rlhf-book/issues/489#issuecomment-5508733184),
fixed in [PR #528](https://github.com/natolambert/rlhf-book/pull/528)).
The first full `kl1` / `kl2` / `kl3` tables in REPORT used that buggy code.

## 1. What was wrong, and what the fix does

Training samples come from the current policy $\pi$. The quantity we want
is forward KL against a frozen reference:

$$
\mathrm{KL}(\pi \| \pi_{\mathrm{ref}})
= \mathbb{E}_{x \sim \pi}\big[\log \pi(x) - \log \pi_{\mathrm{ref}}(x)\big]
= \mathbb{E}_\pi\big[\log(\pi / \pi_{\mathrm{ref}})\big].
$$

Schulman’s Monte Carlo estimators of that KL (samples from $\pi$):

| Name | Formula | Notes |
|------|---------|--------|
| k1 | $\log(\pi / \pi_{\mathrm{ref}})$ | unbiased, can be negative |
| k2 | $\tfrac12(\log(\pi / \pi_{\mathrm{ref}}))^2$ | small-KL approximation |
| k3 | $r - \log r - 1$ with $r = \pi_{\mathrm{ref}} / \pi$ | pointwise $\ge 0$ |

PR #528 only changes **k1** and **k3**. **k2 was already consistent.**

**k1.** Old code returned `-(log π − log π_ref)`, i.e. $\log(\pi_{\mathrm{ref}}/\pi)$.
That is the wrong sign for $\mathrm{KL}(\pi\|\pi_{\mathrm{ref}})$. The fix is
`return log_probs - log_probs_ref`.

**k3.** Old code used `log_ratio = log π − log π_ref`, then `exp(s)−1−s`.
That is k3’s shape applied to $s=\log(\pi/\pi_{\mathrm{ref}})$, so when
$\pi \gg \pi_{\mathrm{ref}}$ (common early in RL) the penalty follows
$\exp(\pi/\pi_{\mathrm{ref}})$ and explodes. The definition needs
$r=\pi_{\mathrm{ref}}/\pi$:

```python
# kl1 (correct): log(π / π_ref)
return log_probs - log_probs_ref

# kl3 (correct): r = π_ref / π → r − 1 − log r
log_ratio = log_probs_ref - log_probs
return torch.expm1(log_ratio) - log_ratio
```

Old code for contrast:

```python
# kl1 (wrong): negated
return -(log_probs - log_probs_ref)

# kl3 (wrong): ratio flipped
log_ratio = log_probs - log_probs_ref
return (log_ratio.exp() - 1) - log_ratio
```

`expm1` vs `exp()−1` is numerical; the real bug is the **ratio direction**.

So the first-run story “kl3 is less stable / lower correctness than kl1/kl2”
is not a result about Schulman k3. Those spikes sit on the **wrong**
exponential path. A rerun on the PR #528 formulas is the comparison that
counts; see [REPORT.md](REPORT.md) for the active `compare_group`.

Putting $\beta \cdot \mathrm{kl}$ in the **training loss** can still give
large gradients when ratios are extreme. That is $\beta$ / penalty scale,
not “the estimator was implemented backwards.”

## 2. KL vs importance sampling (same ratio, different job)

I would not read k3 as “off-policy IS copied into the KL loss.”

If we sample from $\pi$ and write

$$
\rho_{\pi \to \pi_{\mathrm{ref}}} = \frac{\pi_{\mathrm{ref}}}{\pi},
$$

then, algebraically,

$$
\mathrm{KL}(\pi \| \pi_{\mathrm{ref}})
= \mathbb{E}_\pi\big[-\log \rho_{\pi \to \pi_{\mathrm{ref}}}\big].
$$

k1 as $\log(\pi/\pi_{\mathrm{ref}})$ is the same as $-\log(\pi_{\mathrm{ref}}/\pi)$.
Schulman’s $r=p/q$ with $q=\pi$, $p=\pi_{\mathrm{ref}}$ is that $\rho$.

That is only a **shared ratio**. Off-policy IS uses $\rho$ (or $\pi/b$) as a
**multiplicative weight on return**. The KL term **averages a function of
the log-ratio** (k1 / k2 / k3). Same pair of policies, two different
objects.

## 3. BTW: Two variance stories and same problem

**IS on returns.** Variance is large mainly because of **trajectory
weights**: $\rho_{t:T-1}=\prod_k \pi/b$, unbounded when $b(a\mid s)$ is
tiny, then multiplied onto $G$. Long products, not a token-wise KL.

**k1 as a KL estimator.** Usually **token-level** $\log(\pi/\pi_{\mathrm{ref}})$,
not a product along the episode. Variance is large because (1) true KL
$\ge 0$ but a single sample can be **negative**, so signs cancel, and
(2) the log-ratio under $\pi$ is **heavy-tailed**. k3’s
$r-\log r-1$ is pointwise $\ge 0$ and is the usual lower-variance MC
estimator of the same KL. $\pi$ in the denominator of $r$ is that
estimator, not Sutton’s “behavior in the denominator ⇒ IS must explode.”
