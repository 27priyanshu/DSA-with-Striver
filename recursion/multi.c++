#include <bits/stdc++.h>
using namespace std;
int func(int n)
{
    if (n <= 1)
        return n;
    int last = func(n - 1);
    int slast = func(n - 2);
    return last + slast;
}

int main()
{
    int n = 4;
    func(n);
    cout << func(4);
    return 0;
}
//multiple recursion output = 3