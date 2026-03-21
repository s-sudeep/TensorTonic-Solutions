import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    ev = 0
    x,p = np.array(x), np.array(p)

    if not np.isclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Probabilities must sum to 1.")
        
    ev = np.dot(x, p)
    
    return float(ev)