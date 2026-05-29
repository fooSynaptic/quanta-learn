# SVM SMO 求解算法

本目录用于整理支持向量机（SVM）对偶问题的 SMO（Sequential Minimal Optimization）求解思路与线性核实现。

<a id="toc"></a>

## 目录

- [目录结构](#sec-structure)
- [一、优化目标](#sec-1)
- [二、SMO 核心流程](#sec-2)
- [三、关键约束](#sec-3)
- [四、代码对应关系](#sec-4)
- [五、运行演示](#sec-5)
- [六、一句话总结](#sec-6)
- [附录 A：$\alpha_b$ 无约束最优公式推导](#appendix-alpha-b-unc)
- [附录 B：二变量子问题目标 $W(\alpha_a,\alpha_b)$ 的展开](#appendix-w-expansion)
- [附录 C：$\partial W/\partial\alpha_i$ 与 $y_iE_i$ 的严格关系（偏置 $b$ 的去向）](#appendix-grad-bias)

<a id="sec-structure"></a>

## 目录结构

```text
machine_learning/svm/
├── README.md      # 理论说明、约束推导和运行方式
├── smo_flow.svg   # SMO 求解流程图
└── smo_svm.py     # 线性核 SMO 求解器与最小演示数据
```

<a id="sec-1"></a>

## 一、优化目标

软间隔 SVM 的对偶问题可以写成：

$$
\min_{\alpha}\frac{1}{2}\sum_i\sum_j\alpha_i\alpha_jy_iy_jK(x_i,x_j)-\sum_i\alpha_i
$$

约束为：

$$
\sum_i y_i\alpha_i=0,\qquad 0\le\alpha_i\le C
$$

其中：

- $\alpha_i$ 是每个样本对应的拉格朗日乘子。
- $C$ 控制软间隔惩罚强度。
- $K(x_i,x_j)$ 是核函数，本实现使用线性核 $K(x_i,x_j)=x_i^\top x_j$。

<a id="sec-2"></a>

## 二、SMO 核心流程

SMO 每次只优化两个变量 $\alpha_a,\alpha_b$：等式约束 $\sum_i y_i\alpha_i=0$ 在固定其余 $\alpha$ 后，$\alpha_a$ 与 $\alpha_b$ 中只需显式更新一个，另一个由约束唯一确定。

### 本轮用到的符号

| 符号 | 含义 |
|------|------|
| $f(x_i)$ | 当前模型在样本 $i$ 上的决策值（未取符号），见 `decision_function` |
| $E_i$ | **预测误差** $E_i=f(x_i)-y_i$；$E_i=0$ 表示样本恰在间隔边界上 |
| $E_a,E_b$ | 本轮待优化的一对样本 $a,b$ 的误差 |
| $L,H$ | 在等式约束下，只动 $\alpha_b$ 时仍能保证 $0\le\alpha_a,\alpha_b\le C$ 的 **$\alpha_b$ 下界与上界**（由旧 $\alpha_a,\alpha_b$ 与 $y_a,y_b$ 推出，分 $y_a=y_b$ / $y_a\ne y_b$ 两种情形，见第三节） |
| $\eta$ | 二变量子问题二次项系数 $K_{aa}+K_{bb}-2K_{ab}$，$\eta>0$ 时才有稳定的解析步长 |

**为何用 $|E_a-E_b|$ 选 $\alpha_b$？** 在固定 $\alpha_a$ 的等式约束下，$\alpha_b$ 的无约束最优增量与 $(E_a-E_b)/\eta$ 成正比（见 [附录 A](#appendix-alpha-b-unc)）；$|E_a-E_b|$ 越大，沿该方向更新 $\alpha_b$ 的步子通常越大，更容易在一次 pair 优化里明显减小目标。

### 整体流程（与 `smo_svm.py` 一致）

**A. 外层扫描（`fit`）**

1. 交替做「全量样本扫描」与「仅非边界样本 $0<\alpha_i<C$ 扫描」。
2. 对每个候选 $a$，调用 `_examine_example(a)`：若 $\alpha_a$ **未**明显违背 KKT，则跳过；否则进入 B。

**B. 内层配对（`_examine_example`）**

3. 若存在至少两个非边界样本，先在其中选使 **$|E_a-E_b|$ 最大** 的 $b$，尝试一次 `_optimize_pair(a,b)`；成功则结束本轮 $a$。
4. 否则依次尝试：其余非边界样本 → 全训练集，直到某次 pair 更新成功或全部失败。

**C. 单次二变量更新（`_optimize_pair`）**

5. 用当前 $\alpha_a^{old},\alpha_b^{old},y_a,y_b$ 计算 **$L,H$**（$y_a=y_b$ / $y_a\ne y_b$ 两种情形的完整推导见 [$\alpha_b$ 解的边界：$L$ 与 $H$](./alpha_b_solution_boundary.md)）；若 $L=H$，盒约束与等式约束已无自由度，跳过。
6. 算 $\eta$；若 $\eta\le 0$（或过小），跳过本轮 pair。
7. **无约束最优**：$\alpha_b^{new,\text{unc}}=\alpha_b^{old}+y_b(E_a-E_b)/\eta$（推导见 [附录 A](#appendix-alpha-b-unc)）。
8. **盒约束裁剪**：$\alpha_b^{new}=\mathrm{clip}(\alpha_b^{new,\text{unc}},\,L,\,H)$；若与旧值几乎不变则跳过。
9. **等式约束反推**：$\alpha_a^{new}=\alpha_a^{old}+y_ay_b(\alpha_b^{old}-\alpha_b^{new})$。
10. 用新的 $\alpha_a,\alpha_b$ 更新偏置 **$b$**（优先采用落在 $(0,C)$ 内的那个 $\alpha$ 对应的 $b$）。

**D. 停止**

11. 重复 A–C，直到一轮扫描中没有任何 $\alpha$ 被更新，且已做过非边界扫描；或达到 `max_iter`。收敛判据即各 $\alpha_i$ 在 `tol` 意义下满足 KKT（见第三节第 4 小节）。

### 求解流程图

下图对应 `smo_svm.py` 中 `fit`、`_examine_example`、`_optimize_pair` 三个核心函数的调用关系：

![SMO 求解流程图](./smo_flow.svg)

<a id="sec-3"></a>

## 三、关键约束

### 1. 等式约束

固定其他变量后，两个待优化变量必须满足：

$$
y_a\alpha_a+y_b\alpha_b=y_a\alpha_a^{old}+y_b\alpha_b^{old}
$$

因此：

$$
\alpha_a^{new}=\alpha_a^{old}+y_ay_b(\alpha_b^{old}-\alpha_b^{new})
$$

这一步让二变量优化只需要显式求解 $\alpha_b$。

### 2. 盒约束 L/H

对应流程 C 的第 5–8 步：在等式约束 $y_a\alpha_a+y_b\alpha_b=\text{const}$ 下，$\alpha_b$ 只能在 $[L,H]$ 内移动，否则 $\alpha_a$ 会越出 $[0,C]$。公式由旧值 $\alpha_a^{old},\alpha_b^{old}$ 推出：

当 $y_a\neq y_b$：

$$
L=\max(0,\alpha_b^{old}-\alpha_a^{old}),\qquad
H=\min(C,C+\alpha_b^{old}-\alpha_a^{old})
$$

当 $y_a=y_b$：

$$
L=\max(0,\alpha_a^{old}+\alpha_b^{old}-C),\qquad
H=\min(C,\alpha_a^{old}+\alpha_b^{old})
$$

若 $L=H$，说明本轮没有可移动空间，直接跳过。

### 3. eta

线性核下二次项曲率为：

$$
\eta=K_{aa}+K_{bb}-2K_{ab}
$$

当 $\eta\le0$ 或过小时，二变量子问题不适合使用这个解析更新，本实现直接跳过本次 pair（$\eta$ 来自 [附录 A](#appendix-alpha-b-unc) 中 $\alpha_b$ 方向的二次项系数）。

### 4. KKT 收敛条件

外层是否处理样本 $i$，看 $E_i=f(x_i)-y_i$ 与 $\alpha_i$ 是否一致（代码里用 $r_i=E_i y_i$ 与 `tol` 比较）。KKT 本身可概括为：

$$
\begin{cases}
\alpha_i=0 \Rightarrow y_if(x_i)\ge1\\
0<\alpha_i<C \Rightarrow y_if(x_i)=1\\
\alpha_i=C \Rightarrow y_if(x_i)\le1
\end{cases}
$$

代码中用 `tol` 作为容忍误差，避免浮点误差导致训练过程无法停止。

<a id="sec-4"></a>

## 四、代码对应关系

`smo_svm.py` 中的主要方法：

- `fit(X, y)`：训练入口，完成全量样本与非边界样本的交替扫描。
- `_examine_example(a_idx)`：判断 $\alpha_a$ 是否违反 KKT，并选择候选 $\alpha_b$。
- `_optimize_pair(a_idx, b_idx)`：完成一次二变量 SMO 更新。
- `_bounds(...)`：计算 $L/H$。
- `_clip(...)`：裁剪 $\alpha_b$。
- `decision_function(X)`：输出 $f(x)$。
- `predict(X)`：输出 $-1/1$ 分类结果。

<a id="sec-5"></a>

## 五、运行演示

在项目根目录执行：

```bash
python3 machine_learning/svm/smo_svm.py
```

输出会展示：

- 训练后的 `alpha`
- 偏置 `b`
- 线性权重 `w`
- 支持向量
- 训练集准确率
- 两个新样本的预测结果

<a id="sec-6"></a>

## 六、一句话总结

SMO 的核心是：每次找出一个违反 KKT 的变量，再选另一个变量配对，在等式约束和盒约束共同限制下完成二变量解析更新，循环直到所有 $\alpha$ 基本满足 KKT。

<a id="appendix-alpha-b-unc"></a>

## 附录 A：$\alpha_b$ 无约束最优公式推导

本附录说明流程 [C 第 7 步](#sec-2) 中

$$
\alpha_b^{new,\text{unc}}=\alpha_b^{old}+\frac{y_b(E_a-E_b)}{\eta}
$$

从何而来。这里的 $b$ 是**样本下标**（拉格朗日乘子 $\alpha_b$），不是流程 C 第 10 步的偏置 $b$。

**「无约束」**指：已满足等式约束 $y_a\alpha_a+y_b\alpha_b=\text{const}$，但尚未施加盒约束 $0\le\alpha_a,\alpha_b\le C$；第 8 步的 $\mathrm{clip}(\cdot,L,H)$ 才处理后者。

相关附录：[B（$W$ 的展开）](#appendix-w-expansion) · [C（$\partial W/\partial\alpha_i$ 与 $y_iE_i$）](#appendix-grad-bias)

### A.1 二变量子问题

固定其余 $\alpha_i$，本轮只动 $\alpha_a,\alpha_b$。与 README [第一节](#sec-1) 一致，最小化目标在 $(\alpha_a,\alpha_b)$ 上的部分为

$$
W(\alpha_a,\alpha_b)=\frac{1}{2}\bigl(\alpha_a^2K_{aa}+\alpha_b^2K_{bb}+2y_ay_b\alpha_a\alpha_bK_{ab}\bigr)-\alpha_a-\alpha_b+W_0,
$$

其中 $W_0$ 与 $\alpha_a,\alpha_b$ 无关；$y_a,y_b\in\{-1,1\}$，故 $y_a^2=y_b^2=1$。此式由第一节的对偶目标展开而来，**完整推导见 [附录 B](#appendix-w-expansion)**。A.3 中 $\partial W/\partial\alpha_i=y_iE_i$ 的严格化，见 [附录 C](#appendix-grad-bias)。

### A.2 等式约束消元

本轮开始时的可行点记为 $\alpha_a^{old},\alpha_b^{old}$，须保持

$$
y_a\alpha_a+y_b\alpha_b=y_a\alpha_a^{old}+y_b\alpha_b^{old}.
$$

解出（见 [第三节 1](#sec-3)）

$$
\alpha_a=\alpha_a^{old}+y_ay_b\bigl(\alpha_b^{old}-\alpha_b\bigr).
$$

令 $s=y_ay_b$，则 $\dfrac{\partial\alpha_a}{\partial\alpha_b}=-s$。代入 $W$ 后，$W$ 变为**只含 $\alpha_b$ 的一元函数** $W(\alpha_b)$。

### A.3 沿约束线的梯度

A.2 已把 $\alpha_a$ 写成 $\alpha_b$ 的函数 $\alpha_a(\alpha_b)$，于是可把 $W$ 视为**复合函数**

$$
\tilde W(\alpha_b)=W\bigl(\alpha_a(\alpha_b),\,\alpha_b\bigr).
$$

下面要求的是它在约束直线上的**全导数** $dW/d\alpha_b$（沿约束方向真实下降率），而非把 $\alpha_a$ 当常数的偏导 $\partial W/\partial\alpha_b$。

#### A.3.1 偏导 vs 全导

| 记号 | 含义 | 走的方向 |
|------|------|---------|
| $\partial W/\partial\alpha_b$ | 把 $\alpha_a$ **固定**时 $W$ 对 $\alpha_b$ 的变化率 | 沿坐标轴 $\alpha_b$ |
| $dW/d\alpha_b$ | $\alpha_a(\alpha_b)$ **一同变化**后 $\tilde W$ 对 $\alpha_b$ 的变化率 | 沿约束直线 |

A.2 末给出 $d\alpha_a/d\alpha_b=-s$，意味着 $\alpha_b$ 每增 $1$，$\alpha_a$ 被迫变化 $-s$，所以二者**不**相等。

#### A.3.2 链式法则给出全导

把 $\tilde W$ 看作两条路径汇入 $\alpha_b$ 的复合：

- **直接路径**：$\alpha_b$ 自身，权重 $d\alpha_b/d\alpha_b=1$
- **间接路径**：$\alpha_b\to\alpha_a\to W$，权重 $d\alpha_a/d\alpha_b=-s$

多元链式法则将两条贡献相加：

$$
\frac{dW}{d\alpha_b}
=\underbrace{\frac{\partial W}{\partial\alpha_b}\cdot 1}_{\text{直接}}
+\underbrace{\frac{\partial W}{\partial\alpha_a}\cdot\frac{d\alpha_a}{d\alpha_b}}_{\text{经 }\alpha_a\text{ 间接}}
=\frac{\partial W}{\partial\alpha_b}-s\,\frac{\partial W}{\partial\alpha_a}.
$$

> 几何上：等式约束 $y_a\alpha_a+y_b\alpha_b=\text{const}$ 是平面里斜率 $-s$ 的直线，沿这条线挪一步等价于「$\alpha_b$ 加 1、$\alpha_a$ 减 $s$」，把两个方向的偏导按这个比例合成即得上式。

<a id="appendix-a33"></a>

#### A.3.3 偏导的具体形式

对 A.1 中的 $W$ 求两个偏导：

$$
\frac{\partial W}{\partial\alpha_a}=\alpha_aK_{aa}+y_ay_b\alpha_bK_{ab}-1,\qquad
\frac{\partial W}{\partial\alpha_b}=\alpha_bK_{bb}+y_ay_b\alpha_aK_{ab}-1.
$$

决策函数 $f(x_i)=\sum_j\alpha_jy_jK(x_j,x_i)+b$（见 `decision_function`），将其代入可整理为

$$
\frac{\partial W}{\partial\alpha_i}=y_if(x_i)-1=y_iE_i,\qquad E_i=f(x_i)-y_i.
$$

上式为正文沿用的**简写**（严格形式为 $\partial W/\partial\alpha_i=y_iE_i-y_ib$，代入 A.3.2 全导数后 $b$ 项抵消，故 A.3.4 仍成立）。逐步推导见 [附录 C](#appendix-grad-bias)。

#### A.3.4 代入 $\alpha_a^{old},\alpha_b^{old}$

把 A.3.3 的结果代入 A.3.2 的全导数表达式，在本轮起点处：

$$
\left.\frac{dW}{d\alpha_b}\right|_{old}
=y_bE_b-s\,y_aE_a
=y_bE_b-y_by_aE_a
=y_b(E_b-E_a).
$$

这正是后面 A.4 求 $\alpha_b^{new,\text{unc}}$ 所需要的「一阶项」。

### A.4 一元二次型与无约束最优

将 $\alpha_a=\alpha_a^{old}-s(\alpha_b-\alpha_b^{old})$ 代入 $W$，展开可知 $W(\alpha_b)$ 是以 $\alpha_b^{old}$ 为中心的**凸二次函数**（当 $\eta>0$），且

$$
\frac{d^2W}{d\alpha_b^2}=\eta=K_{aa}+K_{bb}-2K_{ab}.
$$

令 $\Delta=\alpha_b-\alpha_b^{old}$，则 $W(\alpha_b)=\dfrac{\eta}{2}\Delta^2+\left.\dfrac{dW}{d\alpha_b}\right|_{old}\Delta+const$。无约束极小满足

$$
\eta\,\Delta+\left.\frac{dW}{d\alpha_b}\right|_{old}=0
\quad\Rightarrow\quad
\Delta=-\frac{y_b(E_b-E_a)}{\eta}=\frac{y_b(E_a-E_b)}{\eta}.
$$

即

$$
\alpha_b^{new,\text{unc}}=\alpha_b^{old}+\frac{y_b(E_a-E_b)}{\eta}.
$$

与 `smo_svm.py` 中 `_optimize_pair` 一致。要求 $\eta>0$（流程 C 第 6 步），否则二次项非正定，该解析步长不可靠。

#### A.4.1 公式怎么读

把上式重新分组为「**起点 + 步长 × 方向**」：

$$
\alpha_b^{new,\text{unc}}=\underbrace{\alpha_b^{old}}_{\text{起点}}+\underbrace{\dfrac{1}{\eta}}_{\text{步长（曲率倒数）}}\cdot\underbrace{y_b\bigl(E_a-E_b\bigr)}_{\text{方向×幅度（带符号）}}.
$$

对照常见的优化记号：

| 部件 | 含义 | 类比 |
|------|------|------|
| $\alpha_b^{old}$ | 本轮起点 | 梯度下降中的「当前点」 |
| $1/\eta$ | 牛顿步长——一阶差除以二阶曲率 | 牛顿法 $-f'/f''$ 中的 $1/f''$ |
| $E_a-E_b$ | 误差差，越大说明 pair 越值得调 | 类似「负梯度」幅度 |
| $y_b\in\{-1,+1\}$ | 符号修正，决定向 $\alpha_b$ 增还是减 | 方向 |

> 由 [A.4](#appendix-alpha-b-unc) 的推导，这正是 **沿等式约束直线 $y_a\alpha_a+y_b\alpha_b=\text{const}$** 的一元凸二次函数 $W(\alpha_b)$ 的精确极小点：「一阶项除以二阶项」的牛顿步。

#### A.4.2 符号速查

| 符号 | 名称 / 读法 | 定义 | 出处 |
|------|------------|------|------|
| $\alpha_b^{old}$ | 旧 alpha_b | 本轮开始时样本 $b$ 的拉格朗日乘子 | `_optimize_pair` 中 `alpha_b_old` |
| $\alpha_b^{new,\text{unc}}$ | 新 alpha_b（无约束） | 仅满足等式约束、未做盒约束裁剪的 $\alpha_b$ | A.4 |
| $y_b\in\{-1,+1\}$ | 标签 | 样本 $b$ 的真实分类 | [一、优化目标](#sec-1) |
| $f(x_i)$ | 决策值 | $f(x_i)=\sum_j\alpha_jy_jK(x_j,x_i)+b$，**未取 sign** | `decision_function` |
| $E_i$ | 预测误差 | $E_i=f(x_i)-y_i$；正→偏高，负→偏低，0→恰在间隔边界 | [二、符号表](#sec-2) |
| $E_a, E_b$ | a/b 的误差 | 本轮 pair 两个样本的 $E_i$ | A.3.4 |
| $K_{ij}$ | 核值 | $K(x_i,x_j)$；线性核下为 $x_i^\top x_j$ | [一、优化目标](#sec-1) |
| $\eta$ | **eta**（希腊字母，读「伊塔」/ˈeɪtə/，**不是 n**） | $\eta=K_{aa}+K_{bb}-2K_{ab}$；线性核下 $=\lVert x_a-x_b\rVert^2$ | [三 3、A.4](#sec-3) |
| $s$ | sign 乘积 | $s=y_ay_b\in\{-1,+1\}$，决定约束直线斜率 $-s$ | A.2 |

#### A.4.3 直觉与边界情况

- **$\eta$ 的几何意义**：在线性核下 $\eta=\lVert x_a-x_b\rVert^2$。两样本在特征空间里**离得越远** → $\eta$ 越大 → 步长 $1/\eta$ 越小，每次走得越保守，避免「两个差异极大的样本一步调过头」。
- **$E_a-E_b$ 的方向**：把 $\alpha_b$ 朝能缩小「a、b 误差差距」的方向调；$y_b$ 把这一调整投到正确的符号上。
- **$|E_a-E_b|$ 越大 → 步子越大**：这就是 [流程 B 第 3 步](#sec-2) 选 $b$ 时偏好「$|E_a-E_b|$ 最大」的根本原因。
- **$\eta\le 0$**：二次项「碗朝下」或退化（典型：$x_a=x_b$ 时 $\eta=0$），公式给出的不再是极小，本实现直接 [跳过本轮 pair](#sec-2)。
- **$\eta\to 0^+$**：曲率极小，步长 $1/\eta$ 极大，会越过 $[L,H]$，紧接着的 [第 8 步 clip](#sec-2) 会把它拉回边界。

#### A.4.4 一句话总览

> **新 $\alpha_b$ = 旧 $\alpha_b$ + 「在两样本核曲率 $\eta$ 上、按预测误差差 $(E_a-E_b)$ 走一个带符号 $y_b$ 的牛顿步」**；之后再做盒约束裁剪与 $\alpha_a$ 反推。

### A.5 与后续步骤的关系

| 步骤 | 作用 |
|------|------|
| 第 7 步 | 上式：仅等式约束下的 $\alpha_b$ 最优 |
| 第 8 步 | $\alpha_b^{new}=\mathrm{clip}(\alpha_b^{new,\text{unc}},L,H)$：满足盒约束 |
| 第 9 步 | $\alpha_a^{new}=\alpha_a^{old}+y_ay_b(\alpha_b^{old}-\alpha_b^{new})$：由等式约束反推 $\alpha_a$ |

返回 [二、SMO 核心流程](#sec-2) · [附录 B](#appendix-w-expansion) · [附录 C](#appendix-grad-bias) · [目录](#toc)

<a id="appendix-w-expansion"></a>

## 附录 B：二变量子问题目标 $W(\alpha_a,\alpha_b)$ 的展开

本附录说明 [附录 A.1](#appendix-alpha-b-unc) 中

$$
W(\alpha_a,\alpha_b)=\frac{1}{2}\bigl(\alpha_a^2K_{aa}+\alpha_b^2K_{bb}+2y_ay_b\alpha_a\alpha_bK_{ab}\bigr)-\alpha_a-\alpha_b+W_0
$$

是如何从 [第一节](#sec-1) 的对偶目标中拆出来的。相关附录：[A（$\alpha_b$ 无约束最优）](#appendix-alpha-b-unc) · [C（偏导与 $y_iE_i$）](#appendix-grad-bias)

### B.1 起点：全局对偶目标

第一节给出（最小化形式）：

$$
\Phi(\alpha)=\frac{1}{2}\sum_{i}\sum_{j}\alpha_i\alpha_jy_iy_jK_{ij}-\sum_{i}\alpha_i,\qquad K_{ij}=K(x_i,x_j).
$$

SMO 本轮只改 $\alpha_a,\alpha_b$，其余 $\alpha_i$（记为集合 $R=\{i\mid i\ne a,b\}$）固定。把 $\Phi$ 视作 $(\alpha_a,\alpha_b)$ 的函数 $W(\alpha_a,\alpha_b)$，并将与 $\alpha_a,\alpha_b$ 无关的项统一记为 $W_0$。

### B.2 按指标分块

把双重求和按 $i,j\in\{a,b\}$ 与 $i,j\in R$ 分成三类：

| 类型 | 形式 | 是否依赖 $\alpha_a,\alpha_b$ |
|------|------|------------------------------|
| **二次主项** | $i,j\in\{a,b\}$ | 含 $\alpha_a^2,\alpha_b^2,\alpha_a\alpha_b$ |
| **交叉项** | 一个指标在 $\{a,b\}$、另一个在 $R$ | 对 $\alpha_a,\alpha_b$ **线性** |
| **常数项** | $i,j\in R$ | 与 $\alpha_a,\alpha_b$ 无关，并入 $W_0$ |

线性项 $-\sum_i\alpha_i$ 拆为 $-\alpha_a-\alpha_b-\sum_{i\in R}\alpha_i$，最后一项也并入 $W_0$。

### B.3 二次主项的逐项展开

$i,j\in\{a,b\}$ 共 4 种组合，每项均带前缀 $\tfrac12$：

| $(i,j)$ | $\tfrac12\alpha_i\alpha_jy_iy_jK_{ij}$ |
|---------|----------------------------------------|
| $(a,a)$ | $\tfrac12\alpha_a^2y_a^2K_{aa}$ |
| $(b,b)$ | $\tfrac12\alpha_b^2y_b^2K_{bb}$ |
| $(a,b)$ | $\tfrac12\alpha_a\alpha_by_ay_bK_{ab}$ |
| $(b,a)$ | $\tfrac12\alpha_a\alpha_by_by_aK_{ba}$ |

利用两个事实：

- 核函数对称：$K_{ab}=K_{ba}$
- 标签平方：$y_a^2=y_b^2=1$

$(a,b)$ 与 $(b,a)$ 两项相等，合并后：

$$
\text{二次主项}=\frac{1}{2}\alpha_a^2K_{aa}+\frac{1}{2}\alpha_b^2K_{bb}+y_ay_b\alpha_a\alpha_bK_{ab}.
$$

提出公因子 $\tfrac12$ 即得 A.1 括号里的形式：

$$
\frac{1}{2}\bigl(\alpha_a^2K_{aa}+\alpha_b^2K_{bb}+2y_ay_b\alpha_a\alpha_bK_{ab}\bigr).
$$

### B.4 交叉项与线性项

交叉项把 $i\in\{a,b\}, j\in R$ 与 $i\in R, j\in\{a,b\}$ 合在一起（同样用 $K_{ij}=K_{ji}$ 抵消因子 $\tfrac12$）：

$$
\sum_{j\in R}\alpha_a y_a\alpha_j y_jK_{aj}+\sum_{j\in R}\alpha_b y_b\alpha_j y_jK_{bj}
=\alpha_a y_a v_a+\alpha_b y_b v_b,
$$

其中

$$
v_i\equiv\sum_{j\in R}\alpha_j y_j K_{ij},\qquad i\in\{a,b\}.
$$

加上之前留下的 $-\alpha_a-\alpha_b$，得到对 $\alpha_a,\alpha_b$ 的**一次项**：

$$
(y_av_a-1)\alpha_a+(y_bv_b-1)\alpha_b.
$$

### B.5 合并为 A.1 的式子

把 B.3 的二次主项、B.4 的一次项与全部常数项 $W_0$ 相加：

$$
W(\alpha_a,\alpha_b)=\frac{1}{2}\bigl(\alpha_a^2K_{aa}+\alpha_b^2K_{bb}+2y_ay_b\alpha_a\alpha_bK_{ab}\bigr)+(y_av_a-1)\alpha_a+(y_bv_b-1)\alpha_b+W_0.
$$

A.1 为简洁起见，把一次项里**与 $v_a,v_b$ 有关的部分也吸收进 $W_0$**（它们对 $\alpha_a,\alpha_b$ 是线性的、且对求二阶导没有贡献），只显式保留来自 $-\sum_i\alpha_i$ 的 $-\alpha_a-\alpha_b$，于是写成：

$$
W(\alpha_a,\alpha_b)=\frac{1}{2}\bigl(\alpha_a^2K_{aa}+\alpha_b^2K_{bb}+2y_ay_b\alpha_a\alpha_bK_{ab}\bigr)-\alpha_a-\alpha_b+W_0.
$$

<a id="appendix-b6"></a>

### B.6 与 A.3 求偏导的衔接

A.1 隐去 $v_a,v_b$ 不影响 A.3 的求导结果——[A.3.3](#appendix-a33) 直接对 $W$（按上方 **B.5 完整形式**）求偏导：

$$
\frac{\partial W}{\partial\alpha_a}=\alpha_aK_{aa}+y_ay_b\alpha_bK_{ab}+y_av_a-1,
$$

而 $\alpha_a y_a K_{aa}+\alpha_b y_b K_{ab}+v_a$ 恰好是 $\sum_j\alpha_j y_j K_{aj}$（含 $R$）。再加上偏置 $b$ 即决策值 $f(x_a)$，于是

$$
\frac{\partial W}{\partial\alpha_a}=y_a\bigl(\alpha_a y_a K_{aa}+\alpha_b y_b K_{ab}+v_a\bigr)-1=y_af(x_a)-y_ab-1=y_aE_a-y_ab,
$$

与 A.3.3 的简写 $y_aE_a$ 差一项 $-y_ab$；为何仍可代入 A.3.4，见 [附录 C](#appendix-grad-bias)。$\alpha_b$ 同理。

> 简言之：A.1 的 $W_0$ 不是「丢掉了什么」，而是吸收了对优化无影响的线性/常数偏移；真正在 A.3 起作用的偏导，自动通过 $f(x_i)$、$E_i$ 把 $v_a,v_b$ 与所有 $R$ 的信息带回来。$y_iE_i$ 简写与 $-y_ib$ 的抵消亦见 [附录 C](#appendix-grad-bias)。

返回 [附录 A.1](#appendix-alpha-b-unc) · [附录 A.3.3](#appendix-a33) · [附录 C](#appendix-grad-bias) · [二、SMO 核心流程](#sec-2) · [目录](#toc)

<a id="appendix-grad-bias"></a>

## 附录 C：$\partial W/\partial\alpha_i$ 与 $y_iE_i$ 的严格关系（偏置 $b$ 的去向）

[附录 A.3.3](#appendix-a33) 与 [附录 B.6](#appendix-b6) 都直接写

$$
\frac{\partial W}{\partial\alpha_i}=y_iE_i,\qquad E_i=f(x_i)-y_i,
$$

省略了一个常数项 $-y_ib$。本附录把这一步**完整展开**：先指出严格形式比 $y_iE_i$ 多了一项 $-y_ib$，再证明该项在 [附录 A.3.2](#appendix-alpha-b-unc) 的**全导数**里**完全抵消**，所以 [A.3.4](#appendix-alpha-b-unc) 的结论仍然成立。相关附录：[A](#appendix-alpha-b-unc) · [B（含 $v_a,v_b$ 的完整 $W$）](#appendix-w-expansion)

### C.1 起点：含 $v_a,v_b$ 的完整 W

沿用 [附录 B.5](#appendix-w-expansion)：

$$
W=\frac{1}{2}\bigl(\alpha_a^2K_{aa}+\alpha_b^2K_{bb}+2y_ay_b\alpha_a\alpha_bK_{ab}\bigr)+(y_av_a-1)\alpha_a+(y_bv_b-1)\alpha_b+W_0,
$$

其中 $v_i=\sum_{j\in R}\alpha_jy_jK_{ij}$，$R=\{j\mid j\ne a,b\}$。

对 $\alpha_a$ 求偏导（$\alpha_b$ 同理）：

$$
\frac{\partial W}{\partial\alpha_a}=\alpha_aK_{aa}+y_ay_b\alpha_bK_{ab}+y_av_a-1.\tag{C.1}
$$

> 注意：若用 A.1 的「精简 W」（把 $y_av_a\alpha_a$ 并入 $W_0$）求偏导，将丢掉 $y_av_a$ 一项，与 $y_aE_a$ 对不上；故此处必须用完整 W。

### C.2 用决策函数化简：出现 $-y_ib$

决策函数（见 `decision_function`）：

$$
f(x_a)=\sum_{j}\alpha_jy_jK_{aj}+b=\alpha_ay_aK_{aa}+\alpha_by_bK_{ab}+v_a+b.
$$

两边乘 $y_a$（$y_a^2=1$）：

$$
y_af(x_a)=\alpha_aK_{aa}+y_ay_b\alpha_bK_{ab}+y_av_a+y_ab.
$$

代回 (C.1)：

$$
\boxed{\;\frac{\partial W}{\partial\alpha_a}=y_af(x_a)-y_ab-1=y_aE_a-y_ab.\;}\tag{C.2}
$$

可见 **严格的偏导比 $y_aE_a$ 多了一项 $-y_ab$**。$\alpha_b$ 同理：

$$
\frac{\partial W}{\partial\alpha_b}=y_bE_b-y_bb.\tag{C.3}
$$

### C.3 $-y_ib$ 在全导数里抵消

把 (C.2)(C.3) 代入 [附录 A.3.2](#appendix-alpha-b-unc) 的全导数公式（$s=y_ay_b$）：

$$
\frac{dW}{d\alpha_b}=\frac{\partial W}{\partial\alpha_b}-s\,\frac{\partial W}{\partial\alpha_a}
=\bigl(y_bE_b-y_bb\bigr)-s\bigl(y_aE_a-y_ab\bigr).
$$

把 $b$ 项单独抽出来：

$$
-y_bb-s\cdot(-y_ab)=-y_bb+y_ay_b\,y_ab=-y_bb+y_bb=0.
$$

（用到 $sy_a=y_ay_b\cdot y_a=y_b$。）

剩下的纯 $E$ 项：

$$
y_bE_b-s\,y_aE_a=y_bE_b-y_b\,E_a=y_b(E_b-E_a).
$$

合起来正是 [附录 A.3.4](#appendix-alpha-b-unc) 的结果：

$$
\boxed{\;\left.\frac{dW}{d\alpha_b}\right|_{old}=y_b(E_b-E_a).\;}
$$

### C.4 几何理解

| 量 | 严格值 | 是否含 $b$ |
|----|--------|------------|
| $\partial W/\partial\alpha_a$ | $y_aE_a-y_ab$ | 是 |
| $\partial W/\partial\alpha_b$ | $y_bE_b-y_bb$ | 是 |
| $dW/d\alpha_b$（沿约束线） | $y_b(E_b-E_a)$ | **否** |

偏置 $b$ 在两条坐标轴方向上各产生一份常数偏移（对应 $-y_ab,-y_bb$），但**沿等式约束直线** $y_a\alpha_a+y_b\alpha_b=\text{const}$ 走时，两份偏移按比例 $(1,-s)$ 合成后恰好抵消。从更高视角看：$b$ 是等式约束 $\sum_iy_i\alpha_i=0$ 的拉格朗日乘子，它对**约束面**内的优化方向没有贡献。

### C.5 A.3.3 / B.6 的「简写」如何理解

| 写法 | 严格性 | 何时安全 |
|------|--------|---------|
| $\partial W/\partial\alpha_i=y_iE_i$ | **省略了 $-y_ib$**，不严格 | 仅用于代入 $dW/d\alpha_b$ 求 $\alpha_b$ 更新方向时，$b$ 会自动抵消 |
| $\partial W/\partial\alpha_i=y_iE_i-y_ib$ | 严格（C.2、C.3） | 任何情况 |
| $dW/d\alpha_b=y_b(E_b-E_a)$ | 严格（C.3 推出） | 直接用于 A.4 求 $\alpha_b^{new,\text{unc}}$ |

因此 A.3.3、B.6 的写法可以视作「在沿约束方向取差时，把不会影响结果的常数项预先约掉」。本附录补上的就是这一约掉过程。

返回 [附录 A.3.3](#appendix-a33) · [附录 B.6](#appendix-b6) · [附录 A](#appendix-alpha-b-unc) · [附录 B](#appendix-w-expansion) · [二、SMO 核心流程](#sec-2) · [目录](#toc)
