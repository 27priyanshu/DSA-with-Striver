#include <bits/stdc++.h>
using namespace std;

int cnt = 0;
void fun()
{
    if (cnt == 3)
        return; // base condition where recursion should stop
    cout << cnt << endl;
    cnt++;
    fun(); // recursion function
}

int main()
{
    fun();
    return 0;
}