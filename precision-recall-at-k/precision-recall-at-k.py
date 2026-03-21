def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    precision = len(set(top_k) & set(relevant)) / k
    recall = len(set(top_k) & set(relevant)) / len(relevant)
    return [precision, recall]