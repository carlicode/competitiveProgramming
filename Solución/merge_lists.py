def merge_lists(A: list, B: list) -> list:
    # Combine the two lists and convert them to a set to remove duplicates
    combined = set(A + B)
    # Return the sorted list of unique elements
    return sorted(combined)
