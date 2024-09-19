import math

def find_lcm(a: int, b: int) -> int:
    # Use the formula LCM(a, b) = abs(a*b) // GCD(a, b)
    return abs(a * b) // math.gcd(a, b)
