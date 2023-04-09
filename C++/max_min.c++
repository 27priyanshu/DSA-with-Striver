#include <bits/stdc++.h>
using namespace std;

int maxx(int A, int B)
{
    if (A > B)
        return A;
    else
        return B;
}

int main()
{
    int A, B;
    cin >> A >> B;
    maxx(A, B);
    return 0;
}