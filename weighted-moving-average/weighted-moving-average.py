def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    wma = []
    l = len(weights)
    weight_sum = sum(weights)
    for i in range(len(values)+1 - l):
        ma = 0
        for j in range(l):
            ma += values[i+j] * weights[j]
        norm = ma / weight_sum
        wma.append(norm)
    return wma
        