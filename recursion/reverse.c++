#include <bits/stdc++.h>
using namespace std;

void rev(int i, int n)
{
    if (i < 1)
        return;
    cout << i << endl;
    rev(i - 1, n);
}

int main()
{
    int n, i;
    cin >> n;
    rev(i, n);
    return 0;
}