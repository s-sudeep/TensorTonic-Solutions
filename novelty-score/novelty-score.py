import numpy as np

def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here
    recommendations, item_counts = np.array(recommendations), np.array(item_counts)
    rec_counts = item_counts[recommendations]

    popularity = rec_counts / n_users

    novelty = -1 * np.log2(popularity)

    return np.mean(novelty)