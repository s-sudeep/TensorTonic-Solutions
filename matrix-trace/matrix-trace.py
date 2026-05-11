import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    diags = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i==j:
                diags+=A[i][j]
    return diags
