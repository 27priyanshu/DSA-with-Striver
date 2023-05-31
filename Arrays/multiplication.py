#NAIVE
n=3
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
C=[]
for i in range(n):
    C.append([0]*n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=a[i][k]*b[k][j]
    print(C)
#STRASSEN
def ikjMatrixProduct(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([0]*n)
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    C[i][j] += A[i][k] * B[k][j]
    return C
def add(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([0]*n)
        for i in range(0, n):
            for j in range(0, n):
                C[i][j]=A[i][j] + B[i][j]
    return C
def subtract(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([0]*n)
        for i in range(0, n):
            for j in range(0, n):
                C[i][j]=A[i][j] - B[i][j]
    return C
def strassenR(A, B):
    n = len(A)
    if n <= LEAF_SIZE:
        return ikjMatrixProduct(A, B)
    else:
        newSize = n // 2
        a11 = []
        a12 = []
        a21 = []
        a22 = []
        b11 = []
        b12 = []
        b21 = []
        b22 = []
        for i in range(newSize):
            a11.append([0]*newSize)
            a12.append([0]*newSize)
            a21.append([0]*newSize)
            a22.append([0]*newSize)
            b11.append([0]*newSize)
            b12.append([0]*newSize)
            b21.append([0]*newSize)
            b22.append([0]*newSize)
            for i in range(0, newSize):
                for j in range(0, newSize):
                    a11[i][j] = A[i][j]
                    a12[i][j] = A[i][j + newSize]
                    a21[i][j] = A[i + newSize][j]
                    a22[i][j] = A[i + newSize][j + newSize]
                    b11[i][j] = B[i][j]
                    b12[i][j] = B[i][j + newSize]
                    b21[i][j] = B[i + newSize][j]
                    b22[i][j] = B[i + newSize][j + newSize]
            p1 = strassenR(add(a11, a22), add(b11, b22))
            p2 = strassenR(add(a21, a22), b11)
            p3 = strassenR(a11, subtract(b12, b22))
            p4 = strassenR(a22, subtract(b21, b11))
            p5 = strassenR(add(a11, a12), b22)
            p6 = strassenR(subtract(a21, a11), add(b11, b12))
            p7 = strassenR(subtract(a12, a22), add(b21, b22))
            c12 = add(p3, p5)
            c21 = add(p2, p4)
            c11 = subtract(add(add(p1, p4), p7), p5)
            c22 = subtract(add(add(p1, p3), p6) , p2)
            C = []
            for i in range(n):
                C.append([0]*n)
            for i in range(0, newSize):
                for j in range(0, newSize):
                    C[i][j] = c11[i][j]
                    C[i][j + newSize] = c12[i][j]
                    C[i + newSize][j] = c21[i][j]
                    C[i + newSize][j + newSize] = c22[i][j]
            return C
def strassen(A, B):
    o=0
    n = len(A)
    while(n>2**o):
        o+=1
        m =2**o
        APrep = []
        for i in range(m):
            APrep.append([0]*m)
        BPrep = []
        for i in range(m):
            BPrep.append([0]*m)
            for i in range(n):
                for j in range(n):
                    APrep[i][j] = A[i][j]
                    BPrep[i][j] = B[i][j]
        CPrep = strassenR(APrep, BPrep)
        C = []
        for i in range(n):
            C.append([0]*n)
            for i in range(n):
                for j in range(n):
                    C[i][j] = CPrep[i][j]
        return C
LEAF_SIZE = 1
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
C = strassen(A, B)
print(C)