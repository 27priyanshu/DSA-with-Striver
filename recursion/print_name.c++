#include <bits/stdc++.h>
using namespace std;

int cnt = 0;
void print()
{
    if (cnt == 5)
        return;
    cout << cnt << " name" << endl;
    cnt++;
    print();
}

int main()
{
    print();
    return 0;
}