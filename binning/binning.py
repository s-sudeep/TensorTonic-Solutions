import math

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    if not values or num_bins < 1:
        return []
    values = sorted(values)
    print(values)
    if values[0]==values[-1]:
        return [0] * len(values)

    width = (values[-1] - values[0]) / num_bins

    binning = []
    for x in values:
        bin_idx = min(math.floor((x - values[0])/width), num_bins - 1)
        binning.append(bin_idx)
    return binning
    