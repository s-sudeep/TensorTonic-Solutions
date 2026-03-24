def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    current_best_idx = models[0]
    for i in range(1, len(models)):
        if models[i]["accuracy"] > current_best_idx["accuracy"]:
            current_best_idx = models[i]
    
        elif models[i]["accuracy"] == current_best_idx["accuracy"]:
            if models[i]["latency"] < current_best_idx["latency"]:
                current_best_idx = models[i]
    
            elif models[i]["latency"] == current_best_idx["latency"]:
                if models[i]["timestamp"] > current_best_idx["timestamp"]:
                    current_best_idx = models[i]
    
    return  current_best_idx["name"]