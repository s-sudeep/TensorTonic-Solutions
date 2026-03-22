def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    rating = []
    for i in items:
        den = (i[1] + min_votes)
        wr = ((i[1] / den)* i[0]) + ((min_votes / den) * global_mean)
        rating.append(wr)

    return rating