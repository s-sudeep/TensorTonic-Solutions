import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    vocabulary = {word:idx for idx, word in enumerate(vocab)}
    out = np.zeros(len(vocab), dtype=int)
    for i in tokens:
        if i in vocabulary:
            idx = vocabulary[i]
            out[idx]+=1
    return out