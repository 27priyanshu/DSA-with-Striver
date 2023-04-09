#include <bits/stdc++.h>
using namespace std;
//this code is done on codestudio by codingninja
int count(int n)
{
    int cont = 0;
    while (n > 0)
    {
        int lastDigit = n % 10;
        cont = cont + 1;
        n = n / 10;
    }  
    return cont;
}

// int main(){
//     count();
//     return 0;
// }