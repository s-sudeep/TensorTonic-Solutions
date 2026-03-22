import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows = len(A)
    cols = len(A[0])

    B = np.zeros((cols, rows), dtype = int)

    for i in range(rows):
        for j in range(cols):
            B[j,i] = A[i][j]

    return B
