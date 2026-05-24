"""Linear SVM trained by Sequential Minimal Optimization (SMO).

This module keeps the implementation intentionally small so the SMO constraints
are easy to read: choose two alphas, optimize one, clip to the box constraint,
recover the other from the equality constraint, and update the bias term.
"""

from __future__ import annotations

import numpy as np


class SMOSVM:
    """Soft-margin binary SVM with a linear kernel and SMO solver.

    Labels must be encoded as ``-1`` and ``1``.
    """

    def __init__(
        self,
        C: float = 1.0,
        tol: float = 1e-3,
        max_iter: int = 100,
        eps: float = 1e-5,
    ) -> None:
        self.C = C
        self.tol = tol
        self.max_iter = max_iter
        self.eps = eps

        self.alpha: np.ndarray | None = None
        self.b = 0.0
        self.X: np.ndarray | None = None
        self.y: np.ndarray | None = None
        self.w: np.ndarray | None = None

    def kernel(self, x1: np.ndarray, x2: np.ndarray) -> float:
        """Linear kernel K(x1, x2)."""
        return float(np.dot(x1, x2))

    def decision_function(self, X: np.ndarray) -> np.ndarray:
        """Return raw SVM scores f(x)."""
        self._check_is_fitted()
        X = np.asarray(X, dtype=float)
        return X @ self.w + self.b

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict labels in {-1, 1}."""
        scores = self.decision_function(X)
        return np.where(scores >= 0, 1, -1)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """Return classification accuracy."""
        y = np.asarray(y, dtype=float)
        return float(np.mean(self.predict(X) == y))

    def support_vectors(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Return support vectors, their labels, and non-zero alphas."""
        self._check_is_fitted()
        mask = self.alpha > self.eps
        return self.X[mask], self.y[mask], self.alpha[mask]

    def fit(self, X: np.ndarray, y: np.ndarray) -> "SMOSVM":
        """Train the SVM using Platt-style SMO scans."""
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        self._validate_training_data(X, y)

        self.X = X
        self.y = y
        self.alpha = np.zeros(X.shape[0], dtype=float)
        self.b = 0.0
        self.w = np.zeros(X.shape[1], dtype=float)

        num_changed = 0
        examine_all = True
        iteration = 0

        while (num_changed > 0 or examine_all) and iteration < self.max_iter:
            num_changed = 0

            if examine_all:
                candidates = range(X.shape[0])
            else:
                candidates = np.where((self.alpha > 0) & (self.alpha < self.C))[0]

            for i in candidates:
                if self._examine_example(int(i)):
                    num_changed += 1

            if examine_all:
                examine_all = False
            elif num_changed == 0:
                examine_all = True

            iteration += 1

        self.w = (self.alpha * self.y) @ self.X
        return self

    def _examine_example(self, a_idx: int) -> bool:
        """Choose alpha_a that violates KKT, then try useful alpha_b values."""
        assert self.alpha is not None and self.X is not None and self.y is not None

        ya = self.y[a_idx]
        aa = self.alpha[a_idx]
        Ea = self._error(a_idx)
        r = Ea * ya

        violates_kkt = (r < -self.tol and aa < self.C) or (r > self.tol and aa > 0)
        if not violates_kkt:
            return False

        non_bound = np.where((self.alpha > 0) & (self.alpha < self.C))[0]
        if len(non_bound) > 1:
            errors = np.array([self._error(i) for i in non_bound])
            b_idx = int(non_bound[np.argmax(np.abs(Ea - errors))])
            if self._optimize_pair(a_idx, b_idx):
                return True

        for b_idx in non_bound:
            if self._optimize_pair(a_idx, int(b_idx)):
                return True

        for b_idx in range(self.X.shape[0]):
            if self._optimize_pair(a_idx, b_idx):
                return True

        return False

    def _optimize_pair(self, a_idx: int, b_idx: int) -> bool:
        """Optimize two alpha variables while all constraints stay valid."""
        assert self.alpha is not None and self.X is not None and self.y is not None

        if a_idx == b_idx:
            return False

        a = a_idx
        b = b_idx
        alpha_a_old = self.alpha[a]
        alpha_b_old = self.alpha[b]
        ya = self.y[a]
        yb = self.y[b]
        Ea = self._error(a)
        Eb = self._error(b)

        L, H = self._bounds(alpha_a_old, alpha_b_old, ya, yb)
        if L == H:
            return False

        Kaa = self.kernel(self.X[a], self.X[a])
        Kbb = self.kernel(self.X[b], self.X[b])
        Kab = self.kernel(self.X[a], self.X[b])
        eta = Kaa + Kbb - 2.0 * Kab
        if eta <= self.eps:
            return False

        alpha_b_new = alpha_b_old + yb * (Ea - Eb) / eta
        alpha_b_new = self._clip(alpha_b_new, L, H)
        if abs(alpha_b_new - alpha_b_old) < self.eps:
            return False

        alpha_a_new = alpha_a_old + ya * yb * (alpha_b_old - alpha_b_new)

        b1 = (
            self.b
            - Ea
            - ya * Kaa * (alpha_a_new - alpha_a_old)
            - yb * Kab * (alpha_b_new - alpha_b_old)
        )
        b2 = (
            self.b
            - Eb
            - ya * Kab * (alpha_a_new - alpha_a_old)
            - yb * Kbb * (alpha_b_new - alpha_b_old)
        )

        self.alpha[a] = alpha_a_new
        self.alpha[b] = alpha_b_new

        if 0 < alpha_a_new < self.C:
            self.b = b1
        elif 0 < alpha_b_new < self.C:
            self.b = b2
        else:
            self.b = (b1 + b2) / 2.0

        self.w = (self.alpha * self.y) @ self.X
        return True

    def _raw_decision_at(self, idx: int) -> float:
        assert self.alpha is not None and self.X is not None and self.y is not None
        kernel_values = self.X @ self.X[idx]
        return float(np.sum(self.alpha * self.y * kernel_values) + self.b)

    def _error(self, idx: int) -> float:
        assert self.y is not None
        return self._raw_decision_at(idx) - self.y[idx]

    def _bounds(
        self,
        alpha_a_old: float,
        alpha_b_old: float,
        ya: float,
        yb: float,
    ) -> tuple[float, float]:
        if ya != yb:
            L = max(0.0, alpha_b_old - alpha_a_old)
            H = min(self.C, self.C + alpha_b_old - alpha_a_old)
        else:
            L = max(0.0, alpha_a_old + alpha_b_old - self.C)
            H = min(self.C, alpha_a_old + alpha_b_old)
        return L, H

    @staticmethod
    def _clip(value: float, lower: float, upper: float) -> float:
        return min(max(value, lower), upper)

    def _validate_training_data(self, X: np.ndarray, y: np.ndarray) -> None:
        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")
        if y.ndim != 1:
            raise ValueError("y must be a 1D array.")
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must contain the same number of samples.")
        if self.C <= 0:
            raise ValueError("C must be positive.")
        if self.max_iter <= 0:
            raise ValueError("max_iter must be positive.")
        labels = set(np.unique(y).tolist())
        if labels != {-1.0, 1.0}:
            raise ValueError("y labels must be encoded as -1 and 1.")

    def _check_is_fitted(self) -> None:
        if self.X is None or self.y is None or self.alpha is None or self.w is None:
            raise RuntimeError("Call fit(X, y) before prediction.")


SMO_SVM = SMOSVM


def demo() -> None:
    """Run a tiny linearly separable example."""
    X = np.array(
        [
            [2.0, 2.0],
            [2.0, 3.0],
            [3.0, 2.0],
            [-2.0, -2.0],
            [-3.0, -2.0],
            [-2.0, -3.0],
        ]
    )
    y = np.array([1, 1, 1, -1, -1, -1])

    model = SMOSVM(C=1.0, tol=1e-3, max_iter=100).fit(X, y)
    sv_X, sv_y, sv_alpha = model.support_vectors()

    print("alpha:", np.round(model.alpha, 4))
    print("b:", round(model.b, 4))
    print("w:", np.round(model.w, 4))
    print("support vectors:", sv_X.tolist())
    print("support labels:", sv_y.astype(int).tolist())
    print("support alphas:", np.round(sv_alpha, 4).tolist())
    print("train accuracy:", model.score(X, y))
    print("predict [[4, 4], [-4, -3]]:", model.predict(np.array([[4, 4], [-4, -3]])).tolist())


if __name__ == "__main__":
    demo()
