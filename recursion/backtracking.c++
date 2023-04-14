#include <bits/stdc++.h>
using namespace std;
// print from 1 to n using backtracking
void f(int i, int n)
{
    if (i < 1)
        return;
    f(i - 1, n); // back tracking function
    cout << i << endl;
}

int main()
{
    int n;
    cin >> n;
    f(n, n);
}