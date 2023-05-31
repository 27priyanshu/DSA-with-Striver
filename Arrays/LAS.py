def Max(a, b):
    if a > b:
        return a
    else:
        return b
def zzis(arr, n):
    las = [[0 for i in range(2)] for j in range(n)]
    for i in range(n):
        las[i][0], las[i][1] = 1, 1
    res = 1
    for i in range(1, n):
        for j in range(0, i):
            if (arr[j] < arr[i] and
                las[i][0] < las[j][1] + 1):
                    las[i][0] = las[j][1] + 1
            if(arr[j] > arr[i] and
                las[i][1] < las[j][0] + 1):
                    las[i][1] = las[j][0] + 1
        if (res < max(las[i][0], las[i][1])):
            res = max(las[i][0], las[i][1])
    return res
arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,7]
n = len(arr)
print("Length of Longest alternating subsequence is",zzis(arr, n))