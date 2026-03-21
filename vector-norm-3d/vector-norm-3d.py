import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v = np.array(v, dtype=float)

    if v.ndim==1:
        v_sum = np.sum(v**2)
    else:
        v_sum = np.sum(v**2, axis=1)

    return np.sqrt(v_sum)

    