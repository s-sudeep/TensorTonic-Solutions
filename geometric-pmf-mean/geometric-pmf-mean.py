import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k)
    pmf = np.where(k >= 1, p * (1 - p)**(k - 1), 0.0)
    mean = 1 / p
    
    return pmf, mean