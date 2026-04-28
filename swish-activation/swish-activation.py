import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x)
    sigm = 1 / (1 + np.exp(-1 * x))
    return x * sigm