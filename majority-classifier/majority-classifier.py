import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    uni, counts = np.unique(y_train, return_counts=True)
    print(uni, counts)
    max_count = np.argmax(counts)
    print(max_count)
    majority = uni[max_count]
    print(majority)
    return np.full(len(X_test), majority)