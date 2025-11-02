# ...existing code...

import math

def is_prime(n: int) -> bool:
    """Return True if n is prime, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        s = input("Enter an integer to check for primality: ").strip()
        num = int(s)
    except ValueError:
        print("Invalid input: please enter a valid integer.")
    else:
        print(f"{num} is prime." if is_prime(num) else f"{num} is not prime.")
# ...existing code...