def strassen_multiply(A, B):
    n = len(A)
    if n == 1:
        return A * B
    else:
        A11 = A[:n//2, :n//2]
        A12 = A[:n//2, n//2:]
        A21 = A[n//2:, :n//2]
        A22 = A[n//2:, n//2:]
        B11 = B[:n//2, :n//2]
        B12 = B[:n//2, n//2:]
        B21 = B[n//2:, :n//2]
        B22 = B[n//2:, n//2:]

        P1 = strassen_multiply(A11 + A22, B11 + B22)
        P2 = strassen_multiply(A21 + A22, B11)
        P3 = strassen_multiply(A11, B12 - B22)
        P4 = strassen_multiply(A22, B21 - B11)
        P5 = strassen_multiply(A11 + A12, B22)
        P6 = strassen_multiply(A21 - A11, B11 + B12)
        P7 = strassen_multiply(A12 - A22, B21 + B22)

        C = np.zeros((n, n))
        C[:n//2, :n//2] = P1 + P4 - P5 + P7
        C[:n//2, n//2:] = P3 + P5
        C[n//2:, :n//2] = P2 + P4
        C[n//2:, n//2:] = P1 - P2 + P3 + P6

        return C

# Function to generate two matrices of the given size with random values


def generate_matrices(size):
    A = np.random.randint(1, 10, size=(size, size))
    B = np.random.randint(1, 10, size=(size, size))
    return A, B

# Main function to compare time taken by both methods for different matrix sizes


def compare_time():
    matrix_sizes = [3, 4, 5, 6, 7, 8]
    naive_times = []
    strassen_times = []

    for size in matrix_sizes:
        A, B = generate_matrices(size)
