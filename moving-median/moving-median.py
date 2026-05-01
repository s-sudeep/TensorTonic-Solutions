import numpy as np

def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    values = np.array(values)
    ws = window_size
    output = [ np.median(values[i:i+ws]) for i in range(len(values) + 1 - ws) ]

    return output
    