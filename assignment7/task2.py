def count_down(n: int) -> None:
    """
    Count down from n to 0, printing each number.
    
    Args:
        n: Starting number (should be positive)
    """
    while n >= 0:
        print(n)
        n -= 1  # Fixed: decrement instead of increment

if __name__ == "__main__":
    try:
        start = int(input("Enter a positive number to count down from: "))
        if start < 0:
            print("Please enter a positive number.")
        else:
            count_down(start)
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")