def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    reference_counts_sum, production_counts_sum = sum(reference_counts), sum(production_counts)
    norm_ref, norm_prod = [], []
    for i,j in zip(reference_counts, production_counts):
        norm_ref.append(i / reference_counts_sum)
        norm_prod.append(j / production_counts_sum)

    tvd = []
    for i, j in zip(norm_ref, norm_prod):
        tvd.append(abs(i - j))

    score = 0.5 * sum(tvd)
    drift_detected = score > threshold

    return {"score": score, "drift_detected": drift_detected}
        
        
        