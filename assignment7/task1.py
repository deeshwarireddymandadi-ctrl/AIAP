def add(a, b):
    """
    Add two numbers together and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print(f"Sum: {result}")
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")