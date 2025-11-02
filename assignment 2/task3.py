# ...existing code...

import math

def area_circle(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)  # Area = π * r^2

def area_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width."""
    return length * width  # Area = length * width

def area_triangle(base: float, height: float) -> float:
    """Calculate the area of a triangle given its base and height."""
    return 0.5 * base * height  # Area = 0.5 * base * height

if __name__ == "__main__":
    shape = input("Enter the shape (circle, rectangle, triangle) to calculate the area: ").strip().lower()
    
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))  # Prompt user for radius
        print(f"The area of the circle is: {area_circle(radius)}")  # Calculate and display area

    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))  # Prompt user for length
        width = float(input("Enter the width of the rectangle: "))    # Prompt user for width
        print(f"The area of the rectangle is: {area_rectangle(length, width)}")  # Calculate and display area

    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))      # Prompt user for base
        height = float(input("Enter the height of the triangle: "))  # Prompt user for height
        print(f"The area of the triangle is: {area_triangle(base, height)}")  # Calculate and display area

    else:
        print("Invalid shape entered. Please enter circle, rectangle, or triangle.")
# ...existing code...