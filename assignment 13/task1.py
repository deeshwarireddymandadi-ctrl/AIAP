import math
import sys

# --- Calculation Logic ---

def area_rectangle(length, width):
    """Calculates the area of a rectangle."""
    return length * width

def area_square(side):
    """Calculates the area of a square."""
    # A square is a rectangle where length == width
    return side * side

def area_circle(radius):
    """Calculates the area of a circle using math.pi."""
    # Using math.pi instead of the hardcoded 3.14 for precision
    return math.pi * radius * radius

# Map shape names to their corresponding functions
SHAPE_CALCULATORS = {
    "rectangle": area_rectangle,
    "square": area_square,
    "circle": area_circle
}

# --- User Input & Validation ---

def get_float_input(prompt):
    """Safely gets a positive float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Dimension must be a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except EOFError:
            print("\nInput cancelled. Exiting.")
            sys.exit(1)

def main():
    """Main function to handle user interaction and calculation."""
    print("--- Geometric Area Calculator ---")

    while True:
        print("\nAvailable shapes: rectangle, square, circle (or type 'exit')")
        shape_choice = input("Enter shape name: ").strip().lower()

        if shape_choice == 'exit':
            break

        if shape_choice not in SHAPE_CALCULATORS:
            print("Unknown shape. Please choose from the available list.")
            continue

        if shape_choice == "rectangle":
            length = get_float_input("Enter the length: ")
            width = get_float_input("Enter the width: ")
            result = area_rectangle(length, width)
            print(f"\nResult: The area of the rectangle is {result:.4f}")

        elif shape_choice == "square":
            side = get_float_input("Enter the side length: ")
            result = area_square(side)
            print(f"\nResult: The area of the square is {result:.4f}")

        elif shape_choice == "circle":
            radius = get_float_input("Enter the radius: ")
            result = area_circle(radius)
            print(f"\nResult: The area of the circle is {result:.4f}")

    print("Thank you for using the Area Calculator. Goodbye!")

if __name__ == "__main__":
    main()