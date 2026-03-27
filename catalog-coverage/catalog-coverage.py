def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    return len(set([j for i in recommendations for j in i]))/n_items if n_items else 0.0