import numpy as np
import time
import matplotlib.pyplot as plt
def multiply_naive(A, B):
    
    n = len(A)
    C= np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                return C
            
            
def strassen(A,B):
    n = len(A)
    if n == 1:
        return A * B
    part = n // 2
    A11 = A[:part, :part]
    A12 = A[:part, part:]
    A21 = A[part:, :part]
    A22 = A[part:, part:]
    B11 = B[:part, :part]
    B12 = B[:part, part:]
    B21 = B[part:, :part]
    B22 = B[part:, part:]
    P = strassen(A11 + A22, B11 + B22)
    Q = strassen(A21 + A22, B11)
    R = strassen(A11, B12 - B22)
    S = strassen(A22, B21 - B11)
    T = strassen(A11 + A12, B22)
    U = strassen(A21 - A11, B11 + B12)
    V = strassen(A12 - A22, B21 + B22)
    C = np.zeros((n, n))
    C[:part, :part] = P + S - T + V
    C[:part, part:] = R + T
    C[part:, :part] = Q + S
    C[part:, part:] = P + R - Q + U
    return C
arr_size = [4,16,32,64,128]
normal_time = []
strassen_time = []
for i in arr_size:
    A = np.random.rand(i, i)
    print("A=",A)
    B = np.random.rand(i, i)
    print("\nB=",B)

    n = 2 ** int(np.ceil(np.log2(i)))
    A_padded = np.zeros((n, n))
    B_padded = np.zeros((n, n))
    A_padded[:i, :i] = A
    B_padded[:i, :i] = B
    start_time = time.time()
    multiply_naive(A_padded, B_padded)
    normal_time.append(time.time() - start_time)
    start_time = time.time()
    strassen(A_padded, B_padded)
    Result=strassen(A_padded, B_padded)
    print("\nResultant matrix:\n",Result)
    strassen_time.append(time.time() - start_time)

plt.plot(arr_size, normal_time, label='Naive Multiplication')
plt.plot(arr_size, strassen_time, label='Strassen Algorithm')
plt.legend()
plt.show()
print("\nBAR CHART")
plt.bar(arr_size, normal_time, width=1.0, label='Naive')
plt.bar(np.array(arr_size)+1.0, strassen_time, width=1.0, label='Strassen')
plt.xlabel('Matrix size (n)')
plt.ylabel('Time taken (seconds)')
plt.legend()
plt.show()
