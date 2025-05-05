#include <bits/stdc++.h>
using namespace std;

class A{
    public:
    ~A(){
        cout << "Base destructor" << endl;
    }
};

class B : public A{
    public:
    ~B(){
        cout << "Child destructor" << endl;
    }
};

int main(){
    B b;
    A* ptr_b = &b;
    // delete b;
}