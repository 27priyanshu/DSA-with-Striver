#include <bits/stdc++.h>
using namespace std;

int main()
{
    int cnt = 0, n;
    cin >> n;
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            cnt++;
            if ((n / i) != i)
                cnt++;
        }
    }
    if (cnt == 2)
        cout << "True";
    else
        cout << "False";
}
