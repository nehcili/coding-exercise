// The goal of this exercise is:
// write the function reverse which consumes an int
// then returns an int whose digits are in reverse
// order. For example
// 123 --> 321
// 100 --> 1
// 2038 --> 8302



#include <iostream>
using namespace std;

int reverse(int);

int main()
{
    int n;

    cout << "enter a number to be reverse:";
    cin >> n;
    
    cout << n << " in reverse is:" << reverse(n) << '\n';
}

// reverse the sequence of digits of n
int reverse(int n)
{
    int ans = 0;
    
    while(n > 0)
    {
        ans = 10 * ans + n % 10;
        
        n = int(n / 10);
    }

    return ans;
}
