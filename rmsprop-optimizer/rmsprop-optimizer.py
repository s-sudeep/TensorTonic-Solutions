import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    s = beta * np.array(s) + (1 - beta) * np.square(g)
    w = w - (lr / np.sqrt(s + eps)) * g

    return (w, s)