#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[10];
    cin >> arr[1];
    int n;
    int largest = arr[0];
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > largest)
        {
            largest = arr[i];
        }
    }
    return largest;
}