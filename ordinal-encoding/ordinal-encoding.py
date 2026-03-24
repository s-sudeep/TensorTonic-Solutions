def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    ord = {}
    for i, v in enumerate(ordering):
        ord[v] = i
    return [ord[v] for v in values]