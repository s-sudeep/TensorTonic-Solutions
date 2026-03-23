def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp, fp, tn, fn = 0,0,0,0
    for i,j in zip(y_true, y_pred):
        if i==j:
            tp+=1
        else:
            fp, fn = fp+1, fn+1
        
    return float((2*tp) / (2*tp + fp + fn))
            