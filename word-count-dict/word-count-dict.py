def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    if sentences==[]:
        return {}
    dict = {}
    for i in sentences:
        for j in i:
            dict[j] = dict.get(j, 0) + 1

    return dict