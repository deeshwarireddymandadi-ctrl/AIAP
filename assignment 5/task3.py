# ...existing code...

def fib_recursive(n: int, trace: list | None = None) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    Definition used: F(0) = 0, F(1) = 1, and for n >= 2: F(n) = F(n-1) + F(n-2).

    Args:
        n: non-negative integer index of the Fibonacci sequence.
        trace: optional list to collect call/return steps for explanation.

    Returns:
        The nth Fibonacci number as an int.
    """
    # Record the function call if trace is provided
    if trace is not None:
        trace.append(f"call fib({n})")

    # Base cases: directly return for n == 0 or n == 1
    if n <= 1:
        result = n
    else:
        # Recursive step: sum of the two previous Fibonacci numbers
        result = fib_recursive(n - 1, trace) + fib_recursive(n - 2, trace)

    # Record the return value if trace is provided
    if trace is not None:
        trace.append(f"return fib({n}) -> {result}")
    return result

if __name__ == "__main__":
    try:
        s = input("Enter a non-negative integer n to compute F(n) (F(0)=0, F(1)=1): ").strip()
        n = int(s)
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            # Warn about exponential runtime for large n when using plain recursion
            if n > 35:
                print("Warning: recursive Fibonacci is exponential time. Results may be slow for large n.")
            show = "n"
            if n <= 12:  # offer trace only for reasonably small n
                show = input("Show recursion trace? (y/n) [small n recommended]: ").strip().lower()
            trace = [] if show == "y" else None

            value = fib_recursive(n, trace)
            print(f"F({n}) = {value}")

            # If trace was collected, print a brief step-by-step explanation
            if trace is not None:
                print("\nRecursion trace (calls and returns):")
                for line in trace:
                    print(line)

            # Short explanation of the algorithm
            print("\nExplanation:")
            print(" - Base cases: F(0)=0 and F(1)=1 are returned directly.")
            print(" - Recursive rule: F(n) = F(n-1) + F(n-2).")
            print(" - Each call asks for two smaller subproblems until base cases are reached.")
            print(" - This simple recursive implementation recomputes many values; use memoization or iteration for large n.")
    except ValueError:
        print("Invalid input: please enter a valid integer.")
# ...existing code...