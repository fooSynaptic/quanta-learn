# Basic

## Problems:
- 在C++中，有那四个与类型转换相关的关键字？各有什么特点，在什么场合下使用？
```txt
面试官：定义一个空的类型，里面没有任何成员变量和成员函数。对该类型求sizeof，得到的结果是多少？
应聘者：答案是1。
面试官：为什么不是0？
应聘者：空类型的实例中不包含任何信息，本来求sizeof应该是0，但是当我们声明该类型的实例的时候，它必须在内存中占有一定的空间，否则无法使用这些实例。至于占用多少内存，由编译器决定。Visual Studio中每个空类型的实例占用1字节的空间。
面试官：如果在该类型中添加一个构造函数和析构函数，再对该类型求sizeof，得到的结果又是多少？
应聘者：和前面一样，还是1。调用构造函数和析构函数只需要知道函数的地址即可，而这些函数的地址只与类型相关，而与类型的实例无关，编译器也不会因为这两个函数而在实例内添加任何额外的信息。
面试官：那如果把析构函数标记为虚函数呢？
应聘者：C++的编译器一旦发现一个类型中有虚拟函数，就会为该类型生成虚函数表，并在该类型的每一个实例中添加一个指向虚函数表的指针。在32位的机器上，一个指针占4字节的空间，因此求sizeof得到4；如果是64位的机器，一个指针占8字节的空间，因此求sizeof则得到8。
```
### 避免复制构造函数的传值操作

### 赋值运算符函数
题目：如下为类型CMyString的声明，请为该类型添加赋值运算符函数
```c++
class CMyString {
  public :
    CMyString (char* pData = NULL) ;
    CMyString (const CMyString& str) ;
    ~CMyString (void) ;
    
  private:
    char* m_pData;
    
  CMyString& CMyString::operator = (const CMyString &str) {
    if(this == &str)
      return *this;
      
    delete []m_pData;
    m_pData = NULL;
    
    m_pData = new char[strlen (str.m_pData) + 1];
    
    strcpy (m_pData, str.m_pData) ;
    
    return *this;
  }
```
在上面的函数中，我们在分配内存之前先用delete释放了实例m_pData的内存，如果此时内存不足导致new char跑出了异常，
m_pData将是一个空指针，这样非常容易导致程序崩溃，违背了异常安全性原则-Exception Safety

要想在复制运算法函数中实现异常安全性，我们有两种方法。
一个简单的办法是我们先用new分配新内容在用delete释放已有的内容。这样只在分配内容成功之后再释放原来的内容，也就是
当分配内存失败时我们能够确保原有实例的数据不会修改。
我们还有一个更好的办法是先创建一个临时实例，再交换临时实例和原来的实例，如下是参考代码：
```c++
cmystring& cmystring::operator = (const cmystring &str) {
  if (this != &str) {
    cmystring strtemp(str);
    
    char* ptemp = strtemp.m_pdata;
    strtemp.m_pdata = m_pdata;
    m_pdata = ptemp;
    }
    
    return *this;
  }
```

### 面试题2:实现singleton模式
***题目：设计一个类，我们只能生成该类的一个实例。***
#### 不好打解法一：只适用于单线程环境
```c++
public sealed class singlenton1 {
  private singleton1 () {}
  
  private static singlenton1 instance = null;
  public static singleton1 Instance {
    get {
      if (instance == null) instance new singlenton1();
      return instance;
      }
    }
  }
```

####  解法二：加上同步锁，虽然可以再多线程环境中工作但是效率不高
```c++
public sealed class singlenton2 {
  private singlenton2 () {}
  
  private static readonly object syncObj = new object();
  
  private static singleton2 instance = null;
  
  public static singleton2 Instance {
    get {
      lock (syncObj) {
        if (instance == null) instance = new singleton2();
        }
      return instance;
      }
    }
  }
```
可行的方案是在加同步锁前后两次判断实例是否存在。

