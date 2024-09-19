def calculate_factorial(n: int) -> int:
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Start factorial product at 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
