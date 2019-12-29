// The goal of this program is to
// record all the info entered and outputs
// all non-repeated entries in the order
// they are entered
//
// exercise involves: vector, struct, passing by reference



#include <iostream>
#include <string>
#include <vector>
using namespace std;

// name = strings entered
// count = number of times it is entered
struct Pair {
    string name;
    int count;
};

// the global dictionary of entries
vector<Pair> pairs;

// returns by reference to allow easy modification (i.e. +1 if the 
// entered phrase is seen. This is really redundent. It's here
// only for practicing passing by reference
int& value(const string& s)
{
    for (int i = 0; i != pairs.size(); i++)
        if (s == pairs[i].name) 
            return pairs[i].count;

    Pair new_pair = { s, 0 };
    pairs.push_back(new_pair);

    return pairs[pairs.size()-1].count;
}

int main()
{

    string str = " ";

    while (str != "quit")
    {
        cout << "Enter a word: ";
        cin >> str;

        if (str == "quit")
            break;
        
        value(str)++;
    }

    for (int i = 0; i != pairs.size(); i++)
        cout << pairs[i].name << " ";

    cout << '\n';

    return 1;
}

