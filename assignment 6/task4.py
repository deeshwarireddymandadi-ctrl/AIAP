def sum_to_n_iterative(n: int) -> int:
    """
    Calculate sum of first n natural numbers using iteration.
    Returns 0 for n <= 0.
    """
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_formula(n: int) -> int:
    """
    Calculate sum of first n natural numbers using formula: n * (n + 1) / 2
    Returns 0 for n <= 0.
    """
    if n <= 0:
        return 0
    return n * (n + 1) // 2

def sum_to_n_recursive(n: int) -> int:
    """
    Calculate sum of first n natural numbers using recursion.
    Returns 0 for n <= 0.
    """
    if n <= 0:
        return 0
    return n + sum_to_n_recursive(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer n: ").strip())
        
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            # Calculate using all three methods
            iter_sum = sum_to_n_iterative(n)
            form_sum = sum_to_n_formula(n)
            
            print(f"\nSum of first {n} numbers:")
            print(f"Using iteration: {iter_sum}")
            print(f"Using formula:   {form_sum}")
            
            # Only use recursion for smaller numbers to avoid stack overflow
            if n <= 1000:
                rec_sum = sum_to_n_recursive(n)
                print(f"Using recursion: {rec_sum}")
            else:
                print("Recursion skipped for large n to avoid stack overflow")
                
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")