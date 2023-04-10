#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int sum = 0, dep = n;

    while (n > 0)
    {
        int last_digit = n % 10;
        n = n / 10;
        sum = sum + (last_digit * last_digit * last_digit);
    }
    if (sum == dep)
    {
        cout << "this is armstrong number";
    }
    else
    {
        cout << "this is not a armstrong number";
    }
    return 0;
}