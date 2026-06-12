import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    pick_index = []
    for enum,i in enumerate(y_true):
        pick_index.append(y_pred[enum][i])
    print(pick_index)
    ln_pi = -np.log(pick_index)
    print(ln_pi)
    return np.mean(ln_pi)
    
        