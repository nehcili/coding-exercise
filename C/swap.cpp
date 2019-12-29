// the purpose of this program is to practice
// and compare reference and pointer
// The goal is to swap two int's a and b
// swap1 takes int*
// swap2 takes int&
//
// The difference being int& declared operators are kind of
// like a constant pointer.

#include <iostream>
using namespace std;

void swap1(int*, int*);
void swap2(int&, int&);

int main()
{
    int a, b;

    cout << "Enter 1 int:";
    cin >> a;

    cout << "Enter another int:";
    cin >> b;

    cout << "swap using pointer:\n";
    swap1(&a,&b);
    cout << a << ", " << b << "\n";


    cout << "swap using address:\n";
    swap2(a, b);
    cout << a << ", " << b << "\n";
}

void swap1(int *a, int *b)
{
    int* c = a;

    a = b;
    b = c;
}

void swap2(int &a, int &b)
{
    int temp = b;

    b = a;
    a = temp;
}
