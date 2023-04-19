#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[10] = {1, 2, 4, 7, 7, 5};

    for (int i = 1; i < 10; i++)
    {
        if (arr[i] >= arr[i - 1])
        {
            cout << "True" << endl;
        }
        else
        {
            return false;
        }
        return true;
    }
}