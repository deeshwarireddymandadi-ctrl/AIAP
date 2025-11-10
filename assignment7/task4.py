class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Calculate and return the area of rectangle."""
        return self.length * self.width
    
    def perimeter(self) -> float:
        """Calculate and return the perimeter of rectangle."""
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    try:
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        
        rect = Rectangle(length, width)
        print(f"\nRectangle Calculations:")
        print(f"Area: {rect.area():.2f}")
        print(f"Perimeter: {rect.perimeter():.2f}")
        
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")