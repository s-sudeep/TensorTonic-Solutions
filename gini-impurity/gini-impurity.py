import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    N_l, N_r = len(y_left), len(y_right)
    N = N_l + N_r
    
    if N == 0:
        return 0.0

    if N_l == 0:
        G_l = 0.0
    else:
        _, l_counts = np.unique(y_left, return_counts=True)
        p_left = l_counts / N_l
        G_l = 1 - np.sum(p_left ** 2)

    if N_r == 0:
        G_r = 0.0
    else:
        _, r_counts = np.unique(y_right, return_counts=True)
        p_right = r_counts / N_r
        G_r = 1 - np.sum(p_right ** 2)

    return ((N_l / N) * G_l) + ((N_r / N) * G_r)