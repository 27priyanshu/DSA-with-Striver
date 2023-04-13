#include <bits/stdc++.h>
using namespace std;

void name(int i, int n)
{
    if (i > n)
        return;
    cout << "priyanshu" << endl;
    name(i + 1, n);
}

int main()
{
    int n, i;
    cin >> n;
    name(i, n);
    return 0;
}