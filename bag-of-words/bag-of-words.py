import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    counter = {}
    for i in tokens:
        counter[i] = counter.get(i,0) + 1 if i in vocab else 0

    vector_list = [counter.get(word, 0) for word in vocab]
    return np.array(vector_list, dtype=int)