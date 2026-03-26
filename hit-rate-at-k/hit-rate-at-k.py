def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hits = 0
    users = len(recommendations)
    for i,j in zip(recommendations, ground_truth):
        top_k = i[:k]
        if set(top_k) & set(j):
            hits+=1
    return hits/users if users > 0 else 0.0
        