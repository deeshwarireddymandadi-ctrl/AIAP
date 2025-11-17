# ...existing code...
def safe_divide(numerator, denominator):
    """Divide two numbers after validating inputs.
    Args:
        numerator: numeric value or string convertible to float
        denominator: numeric value or string convertible to float
    Returns:
        float: result of numerator / denominator
    Raises:
        ValueError: if inputs are not numeric
        ZeroDivisionError: if denominator is zero
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        raise ValueError("Both numerator and denominator must be numbers.")
    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return num / den
def main():
    print("=== Safe Division ===")
    try:
        a = input("Enter numerator: ").strip()
        b = input("Enter denominator: ").strip()
        result = safe_divide(a, b)
    except ZeroDivisionError as err:
        print(f"Error: {err}")
        return
    except ValueError as err:
        print(f"Error: {err}")
        return
    print(f"Result: {result}")
if __name__ == "__main__":
    main()
# ...existing code...
# filepath: c:\Users\sunil\OneDrive\Desktop\AIAPS\assignment-10\task5.py
# ...existing code...
def safe_divide(numerator, denominator):
    """Divide two numbers after validating inputs.
    Args:
        numerator: numeric value or string convertible to float
        denominator: numeric value or string convertible to float
    Returns:
        float: result of numerator / denominator
    Raises:
        ValueError: if inputs are not numeric
        ZeroDivisionError: if denominator is zero
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        raise ValueError("Both numerator and denominator must be numbers.")
    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return num / den
def main():
    print("=== Safe Division ===")
    try:
        a = input("Enter numerator: ").strip()
        b = input("Enter denominator: ").strip()
        result = safe_divide(a, b)
    except ZeroDivisionError as err:
        print(f"Error: {err}")
        return
    except ValueError as err:
        print(f"Error: {err}")
        return
    print(f"Result: {result}")
if __name__ == "__main__":
    main()
# ...existing code...