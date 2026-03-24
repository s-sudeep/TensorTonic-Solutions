import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    var = (np.sum(np.square(np.subtract(x, np.mean(x))))) / (len(x) - 1)
    stdev = np.sqrt(var)
    return var, stdev