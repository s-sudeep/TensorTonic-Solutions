import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p, y = np.array(p), np.array(y)
    epsilon = 1e-12
    p = np.clip(p, epsilon, 1.0 - epsilon)
    loss = -y * ((1 - p) ** gamma) * np.log(p) - (1 - y) * (p ** gamma) * np.log(1 - p)
    
    return np.mean(loss)
