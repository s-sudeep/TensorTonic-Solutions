import numpy as np

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assign = []
    for i in points:
        sqrd_dist = []
        for j in centroids:
            sqrd_dist.append(np.sum(np.square(np.subtract(i, j))))
        assign.append(int(np.argmin(sqrd_dist)))
    return assign
        