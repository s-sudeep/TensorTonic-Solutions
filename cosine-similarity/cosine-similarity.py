import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    na,nb = np.linalg.norm(a), np.linalg.norm(b)
    return np.dot(a,b)/(na*nb) if na*nb else 0.0