import numpy as np
import time
import matplotlib.pyplot as plt

# Naive matrix multiplication function
def naive_multiply(A, B):
    C = np.zeros((len(A), len(B[0])))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C
