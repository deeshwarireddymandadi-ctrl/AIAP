def divide(a: float, b: float) -> float:
    """
    Safely divide two numbers, handling division by zero.
    
    Args:
        a: numerator
        b: denominator
        
    Returns:
        Result of a/b
        
    Raises:
        ZeroDivisionError: if b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def safe_divide(a: float, b: float) -> str:
    """
    Wrapper function that handles division errors gracefully.
    """
    try:
        result = divide(a, b)
        return f"Result: {result}"
    except ZeroDivisionError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    try:
        num = float(input("Enter numerator: "))
        den = float(input("Enter denominator: "))
        
        print(safe_divide(num, den))
        
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")