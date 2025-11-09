def cm_to_inches(cm: float) -> float:
    """
    Convert centimeters to inches.
    1 inch = 2.54 centimeters
    
    Example:
        Input: 25.4 cm
        Output: 10.0 inches
    """
    return cm / 2.54

if __name__ == "__main__":
    try:
        cm = float(input("Enter length in centimeters: ").strip())
        if cm < 0:
            print("Please enter a positive value.")
        else:
            inches = cm_to_inches(cm)
            print(f"{cm} centimeters = {inches:.2f} inches")
    except ValueError:
        print("Invalid input. Please enter a valid number.")