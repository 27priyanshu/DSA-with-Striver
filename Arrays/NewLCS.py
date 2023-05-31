def lcs(A, B, n, l):
    L = []
    for i in range(n + 1):
        L.append([0] * (l + 1))
        for i in range(n + 1):
            for j in range(l + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif A[i - 1] == B[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else: L[i][j] = max(L[i - 1][j], L[i][j - 1])
    lcs_string = ""
    i=n
    j=l
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs_string = A[i - 1] + lcs_string
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return L[n][l], lcs_string
count1=count2 = 0
S1 = input("Enter first string: ")
S2 = input("Enter second string: ")
for i in S1:
    count1 += 1
for i in S2:
    count2 += 1
n = count1
l = count2
lcs_length, lcs_string = lcs(S1, S2, n, l)
print("Longest common subsequence is:", lcs_string)
print("Length of Longest common subsequence is", lcs_length)