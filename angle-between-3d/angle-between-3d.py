import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    if np.linalg.norm(v) < 10**-10 or np.linalg.norm(w) < 10**-10:
        return np.nan
    return np.arccos((np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))))