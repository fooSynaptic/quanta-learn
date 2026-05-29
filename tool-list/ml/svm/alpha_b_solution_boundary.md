# SMO 算法中 L 和 H 的推导与确认
核心一句话：**L 和 H 是在等式约束 $y_a\alpha_a + y_b\alpha_b = \text{常数}$ 和盒约束 $0\le\alpha_a,\alpha_b\le C$ 下，$\alpha_b$ 能取到的最小/最大值**，确保更新后 $\alpha_a$ 仍在合法区间内。

---

## 一、基础前提
SMO 中，我们固定其他 $\alpha_i$，只优化 $\alpha_a$ 和 $\alpha_b$，它们必须同时满足两个约束：
1.  **等式约束**：$y_a\alpha_a + y_b\alpha_b = y_a\alpha_a^{old} + y_b\alpha_b^{old}$（由 $\sum\alpha_i y_i=0$ 推导而来，优化过程中保持不变）
2.  **盒约束**：$0\le\alpha_a\le C,\ 0\le\alpha_b\le C$

我们的目标是：用等式约束消去 $\alpha_a$，再结合盒约束，推导出 $\alpha_b$ 的合法区间 $[L,H]$。

---

## 二、分两种情况推导（$y_a \ne y_b$ 和 $y_a = y_b$）
### 情况1：$y_a \ne y_b$（符号相反，即一个+1，一个-1）
1.  由等式约束：
    $$
    y_a\alpha_a + y_b\alpha_b = y_a\alpha_a^{old} + y_b\alpha_b^{old}
    $$
    两边同乘 $y_a$（$y_a^2=1$）：
    $$
    \alpha_a + y_a y_b\alpha_b = \alpha_a^{old} + y_a y_b\alpha_b^{old}
    $$
    因为 $y_a \ne y_b$，所以 $y_a y_b = -1$，代入得：
    $$
    \alpha_a - \alpha_b = \alpha_a^{old} - \alpha_b^{old}
    $$
    整理得：
    $$
    \alpha_a = \alpha_a^{old} - \alpha_b^{old} + \alpha_b
    $$

2.  结合盒约束 $0\le\alpha_a\le C$：
    - 下限约束：$0 \le \alpha_a^{old} - \alpha_b^{old} + \alpha_b$
      $$
      \alpha_b \ge \alpha_b^{old} - \alpha_a^{old}
      $$
    - 上限约束：$\alpha_a^{old} - \alpha_b^{old} + \alpha_b \le C$
      $$
      \alpha_b \le C + \alpha_b^{old} - \alpha_a^{old}
      $$

3.  再结合 $\alpha_b$ 自身的盒约束 $0\le\alpha_b\le C$，取交集：
    $$
    L = \max\left(0,\ \alpha_b^{old} - \alpha_a^{old}\right)
    $$
    $$
    H = \min\left(C,\ C + \alpha_b^{old} - \alpha_a^{old}\right)
    $$

---

### 情况2：$y_a = y_b$（符号相同，同为+1或同为-1）
1.  同理，由等式约束：
    $$
    y_a\alpha_a + y_b\alpha_b = y_a\alpha_a^{old} + y_b\alpha_b^{old}
    $$
    两边同乘 $y_a$，$y_a y_b = 1$，得：
    $$
    \alpha_a + \alpha_b = \alpha_a^{old} + \alpha_b^{old}
    $$
    整理得：
    $$
    \alpha_a = \alpha_a^{old} + \alpha_b^{old} - \alpha_b
    $$

2.  结合盒约束 $0\le\alpha_a\le C$：
    - 下限约束：$0 \le \alpha_a^{old} + \alpha_b^{old} - \alpha_b$
      $$
      \alpha_b \le \alpha_a^{old} + \alpha_b^{old}
      $$
    - 上限约束：$\alpha_a^{old} + \alpha_b^{old} - \alpha_b \le C$
      $$
      \alpha_b \ge \alpha_a^{old} + \alpha_b^{old} - C
      $$

3.  再结合 $\alpha_b$ 自身的盒约束 $0\le\alpha_b\le C$，取交集：
    $$
    L = \max\left(0,\ \alpha_a^{old} + \alpha_b^{old} - C\right)
    $$
    $$
    H = \min\left(C,\ \alpha_a^{old} + \alpha_b^{old}\right)
    $$

---

## 三、关键结论与边界处理
1.  **L 和 H 的意义**：
    它们是 $\alpha_b$ 在同时满足等式约束和盒约束下的**可行区间**。如果无约束更新的 $\alpha_b^{new,unc}$ 落在 $[L,H]$ 内，则直接采用；否则用 `clip` 函数裁剪到边界：
    $$
    \alpha_b^{new} = \begin{cases}
    L & \alpha_b^{new,unc} < L \\
    H & \alpha_b^{new,unc} > H \\
    \alpha_b^{new,unc} & \text{其他}
    \end{cases}
    $$

2.  **边界特殊情况**：
    - 若 $L=H$，说明 $\alpha_b$ 没有任何可移动空间，本轮优化直接跳过。
    - 裁剪后，再通过等式约束反推 $\alpha_a^{new}$，确保 $\alpha_a$ 仍在 $[0,C]$ 内。

---

## 四、验证示例
假设 $C=1$，$\alpha_a^{old}=0.3$，$\alpha_b^{old}=0.5$：
- 若 $y_a \ne y_b$：
  $L=\max(0,0.5-0.3)=0.2$，$H=\min(1,1+0.5-0.3)=1$，$\alpha_b$ 只能在 $[0.2,1]$ 内移动；
- 若 $y_a = y_b$：
  $L=\max(0,0.3+0.5-1)=0$，$H=\min(1,0.3+0.5)=0.8$，$\alpha_b$ 只能在 $[0,0.8]$ 内移动。

两种情况都保证更新后 $\alpha_a$ 不会超出 $[0,C]$。

---

