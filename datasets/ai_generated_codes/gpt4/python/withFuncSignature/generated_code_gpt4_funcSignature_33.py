def sort_third(l: list):
    # Check if the list is empty or contains tuples with less than three elements
    if not l or (any(len(item) < 3 for item in l)):
        return "Invalid input: the list is empty or some tuples do not have a third element."

    # Use sorted function and lambda to sort by the third element of each tuple
    return sorted(l, key=lambda x: x[2])
