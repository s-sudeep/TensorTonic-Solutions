def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    count = {}
    if not sentences:
        return {}
    for i in sentences:
        for j in i:
            print(j)
            count[j] = count.get(j,0) + 1
    return count