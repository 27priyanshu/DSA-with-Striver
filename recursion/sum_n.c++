#include <bits/stdc++.h>
using namespace std;
//sum of first n numbers using parameterised methord
void s(int i, int sum)
{
    if (i < 1)
    {
        cout << sum;
        return;
    }
    s(i - 1, sum + i);
}

int main()
{
    int n;
    cin >> n;
    s(n, 0);
}