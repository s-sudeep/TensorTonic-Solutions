def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    sum_of_categories = {}
    count_of_categories = {}
    for cat,tar in zip(categories, targets):
        sum_of_categories[cat] = sum_of_categories.get(cat, 0) + tar
        count_of_categories[cat] = count_of_categories.get(cat, 0) + 1

    results = []
    for i in categories:
        results.append(sum_of_categories[i] / count_of_categories[i])

    return results