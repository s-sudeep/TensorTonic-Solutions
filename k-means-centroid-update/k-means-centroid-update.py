import numpy as np

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    #tried as a dictionary of point, assignments earlier. It didnt do well
    #now using the hints given
    centre = np.zeros((k, len(points[0])))
    for p, a in zip(points, assignments):
        print(p, a)
        centre[a]  = np.add(centre[a], p)
    print(centre)

    counts = {}
    for a in assignments:
        counts[a] = counts.get(a, 0) + 1
    print(counts)

    for k, v in counts.items():
        centre[k] = np.divide(centre[k], v)

    print(centre)

    return [c.tolist() for c in centre]