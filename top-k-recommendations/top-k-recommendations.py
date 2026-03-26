def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    sc = scores.copy()
    score_with_index = [(j, i) for i, j in enumerate(sc)] 
    
    srt = sorted(score_with_index, key=lambda x: x[0], reverse=True)
    
    final_index = []
    for item in srt:
        if item[1] not in rated_indices:
            final_index.append(item[1])
            
    return final_index[:k]
        