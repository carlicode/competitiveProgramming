def find_second_largest(L: list) -> int:
    # Convert the list to a set to eliminate duplicates
    unique_numbers = set(L)
    
    # If there are fewer than 2 unique numbers, return None
    if len(unique_numbers) < 2:
        return None
    
    # Sort the unique numbers in descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)
    
    # Return the second largest number
    return sorted_numbers[1]
