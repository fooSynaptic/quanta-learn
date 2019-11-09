`
作者：天才儿童
链接：https://www.nowcoder.com/discuss/215883?type=all&order=time&pos=&page=2
来源：牛客网
`



一面：

1、算法题：n个人之间存在m个关系对，关系具有传递性，假如A关注B，B关注C，那么A就间接关注了C。如果一个人被除他之外的所有人都直接或间接关注，那么这个人就是抖音红人，求抖音红人的总数。
---


2、介绍一个你的项目。
---

3、特征选择有哪些方法（介绍项目时涉及到了特征相关性分析，因此问了这个）。
---
PCA, logistic regression, random forest

4、FM是否也能起到自动特征选择的作用，为什么。
---


5、GBDT的原理，和随机森林等算法做比较。
---



二面：

1、svm损失函数推导。
---


2、朴素贝叶斯写公式。
---
prior:
condition: 



3、算法题：两个单链表找到第一个公共结点。
---
casual problem


4、算法题：由0和1组成的二维矩阵，找出1的最大连通域，计算其面积。
---




三面：

1、算法题：长度为n的字符串中包含m个不同的字符，找出包含这m个不同字符的最小子串。
---


2、如果实现c++中的vector，只需push_back和查找两个功能，底层如何实现。
---
```cpp
#include <vector>

using namespace std;

class 

```



3、如果用数组实现，数组初始容量为n，每次push到容量上限之后都扩容到原来的两倍，现在push进去m个数，m远大于n，求相比于m的时间复杂度。
---


4、A和B比赛，A、B获胜的概率分别是0.6、0.4，如果你是A，3局2胜和5局3胜你会选择哪个。
---
排列组合A赢两句（C2/3*(0.6^2 * 0.4)），A赢三局 (C3/3 * (0.6^3))
两者概率相加

5、如果A和B比赛无数局，A获胜的概率是多少。
---



6、有两张表，第一张表有n个专有名词，比如今日头条、抖音等，第二张表有m条query，比如今日头条是怎样的应用、有多少人喜欢刷抖音等，如何统计表1中所有名词在表2中出现的频次。
---


7、一个用户在搜索框输入query之后，如何知道他是否是在找视频。
---

8、如何计算一个微博账户的权威分数。
---

9、介绍一下xgboost有哪些特点。
---


10、xgboost和GBDT的分裂方式你认为哪个好。
---





1、c++中指针和引用的区别。
---
C++ primer中对对象的定义：对象是指一块能存储数据并具有某种类型的内存空间
一个对象a，它有值和地址，运行程序时，计算机会为该对象分配存储空间来存储该对象的值，我们通过该对象的地址，来访问存储空间中的值

指针就是一个对象：它同样有地址和存储的值，只不过，p存储的数据类型是数据的地址，如果我们要以p中存储的数据作为地址来访问对象的值，则要dereference。

我们可以把引用理解成变量的别名。定义一个引用的时候，程序将该引用和它的初始值绑定在一起，而不是拷贝他，因此引用没有额外的地址。

实际上， 引用是一种常量指针，只能绑定到初始化它的对象。



2、如何从用户态进入内核态。
---


3、非线性分类算法有哪些。
---
集合的加法
核方法



4、如何判断一个算法是线性的还是非线性的。
---
线性的定义是f(ax+by) = af(x) + bf(y)，对任意的a,b表现的意义为函数f对加法和数乘两种运算可以交换，或者说这种银蛇保持事物的刚性在平移和伸缩两种变换下，非线性则不保持这种性质
最简单的就是一次函数和二次函数的不同
但是在处理非线性的情况时最喜欢首先将其线性化-泰勒展开，微商代替求导数，或者称之为一种逼近，复杂的用简单的去刻画。


5、算法题：xie一个全排列。
---

6、算法题：长度为n的数组中有一个数字出现了n/2次，快速找到这个数。
---
-solve 1: 遍历整个数组，储存每个数组的出现次数，如果次数大于n/2+1， 直接返回该数字（一次遍历的时间复杂度偏小，但是构建次数的hashmap小号的空间太大）

- solve 2: 充分利用次数等于一般这个特点，使用两个额外的变量candidate和vote，分别代表候选人和票数，遍历数组，如果元素和候选人相同，则vote加一，如果元素和候选人不同，则减去一；如果交掉后票数小于零，则更换候选人为当前元素。
算法的正确性证明： 数组中，数值相同的数都会投赞成票，数值不同的都会投反对票，有一个数出现的次数超过一半，其他书得到的反对票必然大于一半，所以其他树种，任何一个座位candidate得票都会小于零，遭到淘汰，剩下来的只能是一半的那个数
```python
import random

n = 100
nums = [random.randint(100, 150)]*(n//2) + [i for i in range(n//2)]
random.shuffle(nums)

def solution(nums):
    if len(nums) == 0: return 
    candidate, vote = nums[0], 1
    for i, val in enumerate(nums[1:]):
        if val == candidate: vote += 1
        else:
            vote -= 1
        if vote < 0:
            candidate, vote = val, 1
    return candidate


solution(nums)
```

写一个交叉熵
---
熵 求和px log px
交叉熵 求和 p(x)logq(x)
KL散度 求和p(x)logp(x)/q(x)

roc曲线
---
denotes: `roc- reciever operating characteristic Curve`
是false positive rate versuse True positive rate
roc是反映敏感性和特异性关系的曲线
预测准确率为曲线下面的面积


一到n的整数各种可能的排列，逆序为m的情况有多少种。
---
```python
def solution(n, m):
    def permutation(arr):
        if len(arr) <= 1: return [arr]
        ans = []
        for i, val in enumerate(arr):
            tmpArr = arr[:]
            tmpArr.remove(val)
            for j in permutation(tmpArr):
                j.insert(0, val)
                ans.append(j)
        return ans

    arr = [i for i in range(1, n+1)]

    candidateSubArr = permutation(arr)
```
- 求m个逆序对数组的个数
动态规划
我们用 `f(i, j)` 表示数字 `[1 .. i]` 的排列中恰好包含 `j `个逆序对的个数。在状态转移时，我们考虑数` i `放置的位置与逆序对个数的关系。我们在数字 `[1 .. i - 1]` 组成的排列中放入` i` 时，有 `i `种放置方法：如果将` i `放在最后，则逆序对数量不变；如果将` i `放在倒数第二个，则逆序对数量增加 1；如果将` i `放在第一个，则逆序对数量增加 i - 1。这是因为` i `是 `[1 .. i]` 中的最大值，因此将它放置在 `[1 .. i - 1]` 的排列中的任意一个位置，它都会与在它之后的那些数形成逆序对。如果它后面有` k `个数，则会形成` k` 个逆序对。
因此我们可以写出状态转移方程：
***
```
### 背包
f(i, j) = f(i - 1, j)   # 放在最后
     + f(i - 1, j - 1) 
     + ... + 
     f(i - 1, j - i + 1)    #放在最前面， 从(j-i+1)到 j增加了i-1
 ```
***
边界条件为:
`f(i, j0) = 0 if j0 < 0`
`f(0, 0) = 1`
这个动态规划的时间复杂度为 `O(N^2*K)`
，因此我们需要继续优化。可以发现，状态转移方程中的右侧是一段连续的和，我们将 `j `变为 `j - 1`，有：

`f(i, j - 1) = f(i - 1, j - 1) + f(i - 1, j - 2) + ... + f(i - 1, j - i)`
将 `f(i, j) `与 `f(i, j - 1) `相比较，可以得到：
`f(i, j) - f(i - 1, j) = f(i, j - 1) - f(i - 1, j - i)`
==> `f(i, j) = f(i, j - 1) + f(i - 1, j) - f(i - 1, j - i)`
此时使用这个状态转移方程，动态规划的时间复杂度降低为 O(N*K)。
```java
public class Solution {
    public int kInversePairs(int n, int k) {
        int[][] dp = new int[n + 1][k + 1];
        int M = 1000000007;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k && j <= i * (i - 1) / 2; j++) {
                if (i == 1 && j == 0) {
                    dp[i][j] = 1;
                    break;
                } else if (j == 0)
                    dp[i][j] = 1;
                else {
                    int val = (dp[i - 1][j] + M - ((j - i) >= 0 ? dp[i - 1][j - i] : 0)) % M;
                    dp[i][j] = (dp[i][j - 1] + val) % M;
                }
            }
        }
        return dp[n][k];
    }
}


```

```python
class Solution(object):
    def kInversePairs(self, n, m):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
        for i in range(1, n+1):
            for j in range(m+1):
                if not j <= i*(i-1)/2: break

                if i==1 and j==0: 
                    dp[i][j] = 1
                    break
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - (dp[i-1][j-i] if j >= i else 0)

        return dp[n][m]% (10**9+7)
```


树中寻找最近的公共父节点
---
- case1 BST
```python
def nearRoot(root, node1, node2):
    if root.val > node1.val and root.val > node2.val:
        return nearRoot(root.left, node1, node2)
    elif root.val < node1.val and root.val < node2.val:
        return nearRoot(root.right, node1, node2)
    return root
```

- case2 Arbitrary Binary Tree
```python
def nearRoot(root, p, q):
    if not root: return 
    
    if root is p or root is q:
        return root
    
    left = nearRoot(root.left, p, q)
    right = nearRoot(root.right, p, q)
    if left and right:
        return root
    reutrn left or right
```



1、c++程序从启动到运行成功的详细过程；
---
[ref](https://blog.csdn.net/kang___xi/article/details/79571137)

2、java中的finally语句块是否一定会执行；
---
至少有两种情况下finally语句是不会被执行的：
1.try语句没有被执行到，如在try语句之前return就返回了，这样finally语句就不会执行。这也说明了finally语句被执行的必要而非充分条件是：相应的try语句一定被执行到。
2.在try块|catch块中有System.exit(0);这样的语句。System.exit(0)是终止Java虚拟机JVM的，连JVM都停止了，所有都结束了，当然finally语句也不会被执行到。


3、java中的map是否是有序的，要如何实现有序；
---


4、linux中查看进程状态和查看开放端口的命令；
---
lsof -i

5、如果服务器启动的时候我想执行一些命令，该如何实现；
---
crontab?

6、sql语句中的group的处理过程；
---
```sql
select 
    cat
    , sum(sales)
from
    t
where sale_date between "2019/1/1" and "2019/2/2"
group by cat
```
GROUP BY 语句根据一个或多个列对结果集进行分组。
group首先对所有数据根据cat字段分组，然后针对于分组后的数据依赖于聚合函数进行运算，最后再将聚合后的每组数据进行汇总就得到了我们想要的结果。

7、数据库中为什么要定义范式，如果不定义会怎么样；（scheme？）
---
范式：”符合某一种级别的关系模式的集合，表示一个关系内部个属性之间的联系的合理化程度“-一张数据表的表结构所符合的某种设计标准
第一范式：符合第一范式的每个属性都不再可分
第二范式：在第一范式的基础之上消除了非主属性对于码的部分的函数依赖
第三范式：第三范式在第二范式的基础之上消除了非主属性对于码的传递函数依赖
不用范式的话，数据量太大，而且维护起来非常不容易，并且存储了大量不需要的冗余信息



8、随机森林与gbdt的异同；
---
- 从模型框架的角度来看：
梯度提升树GBT 为boosting 模型。
随机森林RF  为bagging 模型。
- 从偏差分解的角度来看：
梯度提升树GBT 采用弱分类器（高偏差，低方差）。梯度提升树综合了这些弱分类器，在每一步的过程中降低了偏差，但是保持低方差。
随机森林RF 采用完全成长的子决策树（低偏差，高方差）。随机森林要求这些子树之间尽可能无关，从而综合之后能降低方差，但是保持低偏差。
如果在梯度提升树和随机森林之间二选一，几乎总是建议选择梯度提升树。

随机森林的优点：
天然的支持并行计算，因为每个子树都是独立的计算。
梯度提升树的优点：
梯度提升树采用更少的子树来获得更好的精度。
因为在每轮迭代中，梯度提升树会完全接受现有树（投票权为1）。而随机森林中每棵树都是同等重要的（无论它们表现的好坏），它们的投票权都是1/N ，因此不是完全接受的。
梯度提升树也可以修改从而实现并行化。
梯度提升树有一个明确的数学模型。因此任何能写出梯度的任务，都可以应用梯度提升树（比如 ranking 任务）。而随机森林并没有一个明确的数学模型。

9、bagging的思想是什么，本质是什么；
---
从偏差-方差分解的角度来看：
Bagging主要关注降低方差，它能平滑强学习器的方差。
因此它在非剪枝决策树、神经网络等容易受到样本扰动的学习器上效果更为明显。
Boosting 主要关注降低偏差，它能将一些弱学习器提升为强学习器。
因此它在SVM 、knn 等不容易受到样本扰动的学习器上效果更为明显。


10、embedding的作用是什么；
---

11、神经网络中的梯度消失和梯度膨胀是什么，怎么解决；
---

12、激活函数的作用；
---
非线性映射

13、如果选出好特征，去掉不好的特征；
---

14、如何检验过拟合，数据量很小怎么办；
---

15、如果线下auc很高，线上各项指标都不好，可能是因为什么，怎么解决。
---
