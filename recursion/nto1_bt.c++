//print from n to 1 using backtracking
#include <bits/stdc++.h>
using namespace std;
                        //dryrun
void f(int i, int n)    // 1,3  2,3  3,3    4,3
{
    if (i > n)          // 1>3  2>3  2>3    4>3 return
        return;
    f(i + 1, n);        // 2,3  3,3  4,3
    cout << i << endl;  //  1    2    3 this gona print
}                       // output will be 3 2 1

int main()
{
    int n;
    cin >> n;
    f(1, n);
}