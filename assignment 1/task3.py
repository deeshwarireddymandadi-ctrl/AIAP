# ...existing code...

def factorial_recursive(n: int) -> int:
    """Recursive factorial.
    Base case: 0! = 1, 1! = 1.
    For n > 1: n! = n * (n-1)!.
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """Iterative factorial using a simple loop.
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        s = input("Enter a non-negative integer to compute factorial: ").strip()
        n = int(s)
        if n < 0:
            print("Invalid input: please enter a non-negative integer.")
        else:
            try:
                rec = factorial_recursive(n)
            except RecursionError:
                rec = "RecursionError (too deep)"
            itr = factorial_iterative(n)
            print(f"{n}! (recursive) = {rec}")
            print(f"{n}! (iterative) = {itr}")
    except ValueError:
        print("Invalid input: please enter a valid integer.")
# ...existing code...