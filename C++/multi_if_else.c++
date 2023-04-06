#include <bits/stdc++.h>
using namespace std;

int main()
{
    int marks;
    cin >> marks;
    if (marks < 25)
    {
        cout << "Your grade is F";
    }
    if (marks >= 25 && marks <= 44)
    {
        cout << "Your grade is E";
    }
    if (marks >= 45 && marks <= 49)
    {
        cout << "Your grade is D";
    }
    if (marks >= 50 && marks <= 59)
    {
        cout << "Your grade is C";
    }
    if (marks >= 60 && marks <= 79)
    {
        cout << "Your grade is B";
    }
    if (marks >= 80 && marks <= 100)
    {
        cout << "Your grade is A";
    }

    return 0;
}