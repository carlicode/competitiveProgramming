def product_except_self(L: list) -> list:
    n = len(L)
    result = [1] * n
    
    # Calculate product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= L[i]
    
    # Calculate product of all elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= L[i]
    
    return result
