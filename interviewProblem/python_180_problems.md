
网上有网友搜集了 180 道 2019 年最新的 Python 面试题解析，让你最短时间内掌握核心知识点，一举通过Python 面试！
1.列出 5 个常用 Python 标准库？
---
ans: numpy, pandas, jieba, gensim, sklearn

2.Python 内建数据类型有哪些？
---
ans: list, set, dict, tuple, string, int, float.

3.简述 with 方法打开处理文件帮我我们做了什么？
---


4.列出 Python 中可变数据类型和不可变数据类型，为什么？
---
- changeable: list, dict.
- unchangeable: int, float, tuple, string.
reference:
```python
>>> x = 1
>>> id(x)
31106520
>>> y = 1
>>> id(y)
31106520
>>> x = 2
>>> id(x)
31106508
>>> y = 2
>>> id(y)
31106508
>>> z = y
>>> id(z)
31106508
>>> x += 2
>>> id(x)
31106484
```
```
    上面这段程序都是对不可变数据类型中的int类型的操作，id()查看的是当前变量的地址值。我们先来看x = 1和y = 1两个操作的结果，从上面的输出可以看到x和y在此时的地址值是一样的，也就是说x和y其实是引用了同一个对象，即1，也就是说内存中对于1只占用了一个地址，而不管有多少个引用指向了它，都只有一个地址值，只是有一个引用计数会记录指向这个地址的引用到底有几个而已。当我们进行x = 2赋值时，发现x的地址值变了，虽然还是x这个引用，但是其地址值却变化了，后面的y = 2以及z = y，使得x、y和z都引用了同一个对象，即2，所以地址值都是一样的。当x和y都被赋值2后，1这个对象已经没有引用指向它了，所以1这个对象占用的内存，即31106520地址要被“垃圾回收”，即1这个对象在内存中已经不存在了。最后，x进行了加2的操作，所以创建了新的对象4，x引用了这个新的对象，而不再引用2这个对象。

    那么为什么称之为不可变数据类型呢？这里的不可变大家可以理解为x引用的地址处的值是不能被改变的，也就是31106520地址处的值在没被垃圾回收之前一直都是1，不能改变，如果要把x赋值为2，那么只能将x引用的地址从31106520变为31106508，相当于x = 2这个赋值又创建了一个对象，即2这个对象，然后x、y、z都引用了这个对象，所以int这个数据类型是不可变的，如果想对int类型的变量再次赋值，在内存中相当于又创建了一个新的对象，而不再是之前的对象。
**不可变数据类型的优点就是内存中不管有多少个引用，相同的对象只占用了一块内存，但是它的缺点就是当需要对变量进行运算从而改变变量引用的对象的值时，由于是不可变的数据类型，所以必须创建新的对象，这样就会使得一次次的改变创建了一个个新的对象，不过不再使用的内存会被垃圾回收器回收。**
```
总结：
```
“python中的不可变数据类型，不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象，内部会有一个引用计数来记录有多少个变量引用这个对象；
可变数据类型，允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。”
```


5.Python 获取当前日期？
---
`import time; time.asctime()`


6.统计字符串每个单词出现的次数
---
`str.count(substr)`

7.用 python 删除文件和用 linux 命令删除文件方法
---
python: os.remove
linux: rm ./filename

8.写一段自定义异常代码
---
```python
try:
    exp
exception as e:
    raise Exception("Got exception with {}".format(e))
```


9.举例说明异常模块中 try except else finally 的相关意义
---
try, except可以用于捕获异常，finally可以作为最终执行的关闭环境和数据流的手段。


10.遇到 bug 如何处理语言特性
---
详细查询异常栈。

1.谈谈对 Python 和其他语言的区别
---


2.简述解释型和编译型编程语言
---
编译型语言：把做好的源程序全部编译成二进制代码的可运行程序。然后，可直接运行这个程序。
解释型语言：把做好的源程序翻译一句，然后执行一句，直至结束！
区别：
编译型语言，执行速度快、效率高；依赖编译器、跨平台性差些。如C、C++、Delphi、Pascal，Fortran。
解释型语言，执行速度慢、效率低；依赖解释器、跨平台性好。如Java、Basic.
通俗的讲，编译语言是在编译后可以直接运行，而解释语言的执行需要一个解释环境。

 java很特殊，java程序也需要编译，但是没有直接编译称为机器语言，而是编译称为字节码，然后用解释方式执行字节码。


3.Python 的解释器种类以及相关特点？
---
- CPython
当从Python官方网站下载并安装好Python2.7后，就直接获得了一个官方版本的解释器：Cpython，这个解释器是用C语言开发的，所以叫CPython，在命名行下运行python，就是启动CPython解释器，CPython是使用最广的Python解释器。
- IPython
IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的，好比很多国产浏览器虽然外观不同，但内核其实是调用了IE。
- PyPy
PyPy是另一个Python解释器，它的目标是执行速度，PyPy采用JIT技术，对Python代码进行动态编译，所以可以显著提高Python代码的执行速度。
- Jython
Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
- IronPython
IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。


4.说说你知道的Python3 和 Python2 之间的区别？
---
python2: xrange, urilib, print
python3: range,, urllib2, print,


5.Python3 和 Python2 中 int 和 long 区别？
---
python2中有long类型
python3中没有long类型，只有int类型



6.xrange 和 range 的区别？
---
在python2中range返回的是一个list，xrange返回一个迭代器
在python3中他们都是返回一个迭代器

**编码规范**
7.什么是 PEP8?
- 为一种python代码编程规范，为了解决不同的python项目中存在不同的变成规范的问题。

8.了解 Python 之禅么？
- import this 会返回python编程设计规范和指导。

9.了解 docstring 么？
- 三个引号包围的文本内容，不同于注释的是docstring不会被解释器忽视，常常应用于PEP代码规范的字符注释。

10.了解类型注解么？
- 函数注解：
    Python 3.5 引入
    对函数的参数进行类型注解
    对函数的返回值进行类型注解
    只对函数参数做一个辅助的说明，并不对函数参数进行类型检查
    提供给第三方工具，做代码分析，发现隐藏的bug
    函数注解的信息，保存在__annotations__属性中
- 变量注解：


11.例举你知道 Python 对象的命名规范，例如方法或者类等
- 不能以数字开头，首字母最好大写，私有类要双下划线或者单下划线开头。

12.Python 中的注释有几种？
- 

13.如何优雅的给一个函数加注释？
14.如何给变量加注释？
15.Python 代码缩进中是否支持 Tab 键和空格混用。
16.是否可以在一句 import 中导入多个库?
17.在给 Py 文件命名的时候需要注意什么?
18.例举几个规范 Python 代码风格的工具数据类型字符串
19.列举 Python 中的基本数据类型？
20.如何区别可变数据类型和不可变数据类型
21.将"hello world"转换为首字母大写"Hello World"
22.如何检测字符串中只含有数字?
23.将字符串"ilovechina"进行反转
24.Python 中的字符串格式化方式你知道哪些？
25.有一个字符串开头和末尾都有空格，比如“ adabdw ”,要求写一个函数把这个字符串的前后空格都去掉。26.获取字符串”123456“最后的两个字符。
27.一个编码为 GBK 的字符串 S，要将其转成 UTF-8 编码的字符串，应如何操作？
28. 
- (1)s="info：xiaoZhang 33 shandong"，用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
- (2) a = "你好 中国 "，去除多余空格只留一个空格。

29. 
- (1)怎样将字符串转换为小写 
- (2)单引号、双引号、三引号的区别？

30.已知 AList = [1,2,3,1,2],对 AList 列表元素去重，写出具体过程。
31.如何实现 "1,2,3" 变成 ["1","2","3"]
32.给定两个 list，A 和 B，找出相同元素和不同元素
33.[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
34.合并列表[1,5,7,9]和[2,2,6,8]
35.如何打乱一个列表的元素？
36.字典操作中 del 和 pop 有什么区别
37.按照字典的内的年龄排序

<img src="https://pic2.zhimg.com/50/v2-f0c87fcad0839af06187a4def1706f51_hd.jpg" data-caption="" data-size="normal" data-rawwidth="834" data-rawheight="124" class="origin_image zh-lightbox-thumb" width="834" data-original="https://pic2.zhimg.com/v2-f0c87fcad0839af06187a4def1706f51_r.jpg"/>

38.请合并下面两个字典 a = {"A":1,"B":2},b = {"C":3,"D":4}
39.如何使用生成式的方式生成一个字典，写一段功能代码。
40.如何把元组("a","b")和元组(1,2)，变为字典{"a":1,"b":2}综合
41.Python 常用的数据结构的类型及其特性？

<img src="https://pic4.zhimg.com/50/v2-3774e05a878688a01233e58eedd189a4_hd.jpg" data-caption="" data-size="normal" data-rawwidth="829" data-rawheight="103" class="origin_image zh-lightbox-thumb" width="829" data-original="https://pic4.zhimg.com/v2-3774e05a878688a01233e58eedd189a4_r.jpg"/>

42.如何交换字典 {"A"：1,"B"：2}的键和值？
43.Python 里面如何实现 tuple 和 list 的转换？
44.我们知道对于列表可以使用切片操作进行部分元素的选择，那么如何对生成器类型的对象实现相同的功能呢？
45.请将[i for i in range(3)]改成生成器
46.a="hello"和 b="你好"编码成 bytes 类型
47.下面的代码输出结果是什么？
<img src="https://pic2.zhimg.com/50/v2-9ece529b1810bbd9052e929e4dbb760a_hd.jpg" data-caption="" data-size="normal" data-rawwidth="837" data-rawheight="59" class="origin_image zh-lightbox-thumb" width="837" data-original="https://pic2.zhimg.com/v2-9ece529b1810bbd9052e929e4dbb760a_r.jpg"/>

48.下面的代码输出的结果是什么?<img src="https://pic2.zhimg.com/50/v2-e8e5e086d9e9c7b45861717d33de5986_hd.jpg" data-caption="" data-size="normal" data-rawwidth="832" data-rawheight="59" class="origin_image zh-lightbox-thumb" width="832" data-original="https://pic2.zhimg.com/v2-e8e5e086d9e9c7b45861717d33de5986_r.jpg"/>

49.Python 交换两个变量的值
50.在读文件操作的时候会使用 read、readline 或者 readlines，简述它们各自的作用
51.json 序列化时，可以处理的数据类型有哪些？如何定制支持 datetime 类型？
52.json 序列化时，默认遇到中文会转换成 unicode，如果想要保留中文怎么办？
53.有两个磁盘文件 A 和 B，各存放一行字母，要求把这两个文件中的信息合并(按字母顺序排列)，输出到一个新文件 C 中。
54.如果当前的日期为 20190530，要求写一个函数输出 N 天后的日期，(比如 N 为 2，则输出 20190601)。
55.写一个函数，接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。
56.下面代码会存在什么问题，如何改进？<img src="https://pic2.zhimg.com/50/v2-474f556cb8cd7d2ea7a47b0cba51c9cd_hd.jpg" data-caption="" data-size="normal" data-rawwidth="834" data-rawheight="125" class="origin_image zh-lightbox-thumb" width="834" data-original="https://pic2.zhimg.com/v2-474f556cb8cd7d2ea7a47b0cba51c9cd_r.jpg"/>
57.一行代码输出 1-100 之间的所有偶数。
58.with 语句的作用，写一段代码？
59.python 字典和 json 字符串相互转化方法
60.请写一个 Python 逻辑，计算一个文件中的大写字母数量
61. 请写一段 Python连接 Mongo 数据库，然后的查询代码。
62.说一说 Redis 的基本类型。
63. 请写一段 Python连接 Redis 数据库的代码。
64. 请写一段 Python 连接 MySQL 数据库的代码。
65.了解 Redis 的事务么？
66.了解数据库的三范式么？
67.了解分布式锁么？
68.用 Python 实现一个 Reids 的分布式锁的功能。
69.写一段 Python 使用 Mongo 数据库创建索引的代码。

**高级特性**
70.函数装饰器有什么作用？请列举说明？
71.Python 垃圾回收机制？
72.魔法函数 __call__怎么使用?
73.如何判断一个对象是函数还是方法？
74.@classmethod 和@staticmethod 用法和区别
75.Python 中的接口如何实现？
76.Python 中的反射了解么?
77.metaclass 作用？以及应用场景？
78.hasattr() getattr() setattr()的用法
79.请列举你知道的 Python 的魔法方法及用途。
80.如何知道一个 Python 对象的类型？
81.Python 的传参是传值还是传址？
82.Python 中的元类(metaclass)使用举例
83.简述 any()和 all()方法
84.filter 方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
85.什么是猴子补丁？
86.在 Python 中是如何管理内存的？
87.当退出 Python 时是否释放所有内存分配？正则表达式
88.使用正则表达式匹配出<html><h1>百度一下，你就知道</html>中的地址   
a="张明 98 分"，用 re.sub，将 98 替换为 100
89.正则表达式匹配中(.*)和(.*?)匹配区别？
90.写一段匹配邮箱的正则表达式其他内容
91.解释一下 python 中 pass 语句的作用？
92.简述你对 input()函数的理解
93.python 中的 is 和==
94.Python 中的作用域
95.三元运算写法和应用场景？
96.了解 enumerate 么？
97.列举 5 个 Python 中的标准模块
98.如何在函数中设置一个全局变量99.pathlib 的用法举例
100.Python 中的异常处理，写一个简单的应用场景
101.Python 中递归的最大次数，那如何突破呢？
102.什么是面向对象的 mro
103.isinstance 作用以及应用场景？
104.什么是断言？应用场景？
105.lambda 表达式格式以及应用场景？
106.新式类和旧式类的区别
107.dir()是干什么用的？
108.一个包里有三个模块，demo1.py, demo2.py, demo3.py，但使用 from tools import *导入模块时，如何保证只有 demo1、demo3 被导入了。
109.列举 5 个 Python 中的异常类型以及其含义
110.copy 和 deepcopy 的区别是什么？
111.代码中经常遇到的*args, **kwargs 含义及用法。
112.Python 中会有函数或成员变量包含单下划线前缀和结尾，和双下划线前缀结尾，区别是什么?
113.w、a+、wb 文件写入模式的区别
114.举例 sort 和 sorted 的区别
115.什么是负索引？
116.pprint 模块是干什么的？
117.解释一下 Python 中的赋值运算符
118.解释一下 Python 中的逻辑运算符
119.讲讲 Python 中的位运算符
120.在 Python 中如何使用多进制数字？
121.怎样声明多个变量并赋值？算法和数据结构
122.已知：<img src="https://pic4.zhimg.com/50/v2-f78e20b47b593dc30d2892c34e1c5a7b_hd.jpg" data-caption="" data-size="normal" data-rawwidth="832" data-rawheight="53" class="origin_image zh-lightbox-thumb" width="832" data-original="https://pic4.zhimg.com/v2-f78e20b47b593dc30d2892c34e1c5a7b_r.jpg"/>(1) 从 AList 和 BSet 中 查找 4，最坏时间复杂度那个大？(2) 从 AList 和 BSet 中 插入 4，最坏时间复杂度那个大？
123.用 Python 实现一个二分查找的函数
124.python 单例模式的实现方法
125.使用 Python 实现一个斐波那契数列
126.找出列表中的重复数字
127.找出列表中的单个数字
128.写一个冒泡排序
129.写一个快速排序
130.写一个拓扑排序
131.python 实现一个二进制计算
132.有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
133.单链表反转
134.交叉链表求交点
135.用队列实现栈
136.找出数据流的中位数
137.二叉搜索树中第 K 小的元素

**爬虫相关**
138.在 requests 模块中，requests.content 和 requests.text 什么区别
139.简要写一下 lxml 模块的使用方法框架
140.说一说 scrapy 的工作流程
141.scrapy 的去重原理
142.scrapy 中间件有几种类，你用过哪些中间件
143.你写爬虫的时候都遇到过什么？反爬虫措施，你是怎么解决的？
144.为什么会用到代理？
145.代理失效了怎么处理？
146.列出你知道 header 的内容以及信息
147.说一说打开浏览器访问 百度一下，你就知道 获取到结果，整个流程。
148.爬取速度过快出现了验证码怎么处理
149.scrapy 和 scrapy-redis 有什么区别？为什么选择 redis 数据库？
150.分布式爬虫主要解决什么问题
151.写爬虫是用多进程好？还是多线程好？ 为什么？
152.解析网页的解析器使用最多的是哪几个
153.需要登录的网页，如何解决同时限制 ip，cookie,session（其中有一些是动态生成的）在不使用动态爬取的情况下？
154.验证码的解决（简单的：对图像做处理后可以得到的，困难的：验证码是点击，拖动等动态进行的？）155.使用最多的数据库（mysql，mongodb，redis 等），对他的理解？网络编程
156.TCP 和 UDP 的区别？
157.简要介绍三次握手和四次挥手
158.什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？

**并发**
159.举例说明 conccurent.future 的中线程池的用法
160.说一说多线程，多进程和协程的区别。
161.简述 GIL
162.进程之间如何通信
163.IO 多路复用的作用？
164.select、poll、epoll 模型的区别？
165.什么是并发和并行？
166.一个线程 1 让线程 2 去调用一个函数怎么实现？
167.解释什么是异步非阻塞？
168.threading.local 的作用？

**Git 面试题**
169.说说你知道的 git 命令
170.git 如何查看某次提交修改的内容