// write count_str that counts the number of pairs in s with s passed as array
// write count_str that counts the number of pairs in s with s passed as a pointer and terminating with '\0'


#include <iostream>
#include <string.h>
using namespace std;

int count_str(char s[], char[]);

int count_char(char* s, char[]);

int main()
{
    char s[1000];
    char pair[3]; // a pair char array has 3 element, last element for '\0', 
    // if you don't do this, something is going to mess up in the memory

    cout << "Enter a string (max len==999): ";
    cin >> s;


    cout << "Enter a pair: ";
    cin >> pair;




    cout << "Passing as an array, there are " << count_str(s, pair) << " occurance of " << pair << "." << endl;
    cout << "Passing as a pointer, there are " << count_char(s, pair) << " occurance of " << pair << "." << endl;


}

int count_char(char* s, char pair[])
{
    int count = 0;
    bool flag = false;

    while (*s != '\0')
    {
        if (flag == true)
        {
            if (*s == pair[1])
                count++;

            flag = false;
        }
        if (*s == pair[0])
            flag = true;

        s++;
    }

    return count;
}


int count_str(char s[], char pair[])
{
    int count = 0;
    bool flag = false;

    for (int i=0; i < strlen(s); i++)
    {
        if (flag == true)
        {
            if (s[i] == pair[1])
                count++;
            
            flag = false;            
        }
        if (s[i] == pair[0])
           flag = true;
    }

    return count;
}
