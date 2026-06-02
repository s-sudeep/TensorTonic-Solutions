import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.zeros((0,0), dtype=int)

    max_l = max_len if max_len is not None else max(len(seq) for seq in seqs)

    res = np.full((len(seqs), max_l), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
        truncate = seq[:max_l]
        res[i, :len(truncate)] = truncate

    return res
        