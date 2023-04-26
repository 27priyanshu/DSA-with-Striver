#include <bits/stdc++.h>
using namespace std;

int LinearSearch(int arr[], int n, int num)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == num)
            return i;
    }
    return -1;
}

int main()
{
    int n = 5;
    int num = 7;
    int arr[n] = {2, 5, 4, 7, 5};

    cout << LinearSearch(arr, n, num);

    return 0;
}