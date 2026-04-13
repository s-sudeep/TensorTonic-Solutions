import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    # su = 0
    # for i in range(len(A)):
    #     for j in range(len(A)):
    #         if i==j:
    #             su+=A[i][j]

    # return su

    return sum([A[i][j] for i in range(len(A)) for j in range(len(A)) if i==j])