def lis(arr):
    n = len(arr)
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
    maximum = max(lis)
    return maximum
arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,7]
print("Length of lis is", lis(arr))