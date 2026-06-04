import numpy as np

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    predictions, targets = np.array(predictions), np.array(targets)
    epsilon = 1e-12
    p = np.clip(predictions, epsilon, 1.0 - epsilon)

    pt = np.where(targets == 1, p, 1 - p)
    FL = -1 * alpha * ((1 - pt)**gamma) * np.log(pt)
    return np.mean(FL)