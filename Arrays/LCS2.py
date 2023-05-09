def lcs(X , Y, m, n):     
    L = []
    for i in range(m+1):
        L.append([0]*(n+1))
    print (L)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]

S1 = "AGGTAB"
S2 = "GXTXAYB"
m = 6
n = 7
print ("Length of LCS is", lcs(S1, S2, m, n))