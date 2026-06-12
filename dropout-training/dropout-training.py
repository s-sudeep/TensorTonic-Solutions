import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    if p>=1:
        return np.zeros_like(x), np.zeros_like(x)
    if rng is not None:
        random_vals = rng.random(x.shape)
    else:
        random_vals = np.random.random(x.shape)

    scale_ft = 1 / (1 - p)
    dropout_pat = np.where(random_vals < (1-p), scale_ft, 0)
    op = x * dropout_pat

    return op, dropout_pat
    