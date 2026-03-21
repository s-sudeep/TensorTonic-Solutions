def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    result = [[] for _ in range(len(values))]

    for i,j in enumerate(values):
        result[i] = [j**k for k in range(degree + 1)]

    return result
        