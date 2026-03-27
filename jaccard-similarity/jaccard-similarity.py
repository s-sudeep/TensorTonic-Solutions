def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    a,b = set(set_a), set(set_b)
    return len((a&b))/len(a|b) if len(a|b) else 0.0