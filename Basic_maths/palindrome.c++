#include <bits/stdc++.h>
using namespace std;

int main()
{
    int revno = 0;
    int n;
    cin >> n;
    int dup = n;
    while (n > 0)
    {
        int last_digit = n % 10;
        revno = (revno * 10) + last_digit;
        n = n / 10;
    };
    if (revno == dup)
    {
        cout << "This is Palindrome";
    }
    else
    {
        cout << "This is not a Palindrome";
    }
}