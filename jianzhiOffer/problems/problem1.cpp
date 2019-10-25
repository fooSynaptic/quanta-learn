#include <iostream>
#include <string>
#include <vector>

using namespace std;

class A{
    private:
        int value;
    
    public:
        A(int n) {value = n;}
        A(A const &other) {value = other.value;}
        //A(A other) {value = other.value;}     ###wrong

        /*
        在上述代码中，复制构造函数A（A other）传入的参数是A的一个实例。
        由于是传值参数，我们吧一个形参复制到实参会调用复制构造函数。
        因此如果允许复制构造函数传值，就会在复制构造函数内调用复制构造函数，
        也就会形成永无休止的递归调用从而导致栈溢出。因此C++的标准不允许
        复制构造函数传值参数，在visual studio和gcc中都会编译错误。
        要解决这个问题，可以将构造函数的传值参数改成常量引用。
        */

        void Print() {
            cout << value << endl;
        }
};



int main(){
    A a = 10;
    A b = a;
    b.Print();
    return 0;

}
