def lcs(X , Y, m, n):
    L = []
    for i in range(m+1):
        L.append([0]*(n+1))
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    continue
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j] , L[i][j-1])
                return L
S1 = "AGGTAB"
S2 = "GXTXAYB"
m = 6
n = 7
L=lcs(S1, S2, m, n)
for i in L:
    print(i,end="\n")
sub=""
while(m>0):
    if L[m-1][n-1]<L[m][n] :
        sub=S1[m-1]+sub
    m-=1
    n-=1
print(sub)