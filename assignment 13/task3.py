import sys

class Student:
    """
    Represents a student with a name, age, and a flexible number of subject marks.
    Improved for readability and modularity.
    """
    def __init__(self, name, age, marks):
        # Improved readability: using descriptive names
        self.name = name
        self.age = age
        
        # Improved modularity: marks are stored as a list, allowing for any number of subjects
        if not all(isinstance(m, (int, float)) for m in marks):
             raise TypeError("All marks must be numerical values.")
        self.marks = marks

    # Use a property decorator for derived attributes (like total), 
    # making them look like simple attributes but calculated dynamically.
    @property
    def total_score(self):
        """Calculates and returns the sum of all marks."""
        return sum(self.marks)

    @property
    def average_score(self):
        """Calculates and returns the average mark."""
        if not self.marks:
            return 0.0
        return self.total_score / len(self.marks)

    def __str__(self):
        """
        Special method to provide a clean, human-readable string representation of the object.
        This replaces the old 'details' method.
        """
        return (
            f"Student Details:\n"
            f"  Name: {self.name}\n"
            f"  Age: {self.age} years\n"
            f"  Marks: {self.marks}\n"
            f"  Total Score: {self.total_score}\n"
            f"  Average Score: {self.average_score:.2f}"
        )

# --- User Input Demonstration ---

def get_string_input(prompt):
    """Safely gets a string input."""
    try:
        return input(prompt).strip()
    except EOFError:
        print("\nInput cancelled. Exiting.")
        sys.exit(0)

def get_age_input(prompt):
    """Safely gets a positive integer for age."""
    while True:
        try:
            age = int(input(prompt).strip())
            if age <= 0:
                print("Age must be a positive number.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")
        except EOFError:
            sys.exit(0)

def get_marks_input():
    """Asks for marks separated by commas."""
    while True:
        try:
            marks_str = get_string_input("Enter subject marks (e.g., 85, 92, 78): ")
            if not marks_str:
                return []
            # Converts comma-separated string into a list of floats
            marks = [float(m.strip()) for m in marks_str.split(',')]
            return marks
        except ValueError:
            print("Invalid input. Please ensure marks are numbers separated by commas.")

def main():
    """Demonstrates the refactored Student class by gathering user inputs."""
    print("--- Student Class Data Entry ---")

    # 1. Get User Inputs
    name = get_string_input("Enter student name: ")
    age = get_age_input("Enter student age: ")
    marks = get_marks_input()
    
    if not name or not marks:
        print("Name and marks are required. Exiting.")
        return

    try:
        # 2. Instantiate the Refactored Class
        student1 = Student(name, age, marks)

        # 3. Display Results using the __str__ method and properties
        print("\n==================================")
        # Calling print() on the object automatically uses the __str__ method
        print(student1)
        print("==================================")
        
    except TypeError as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    main()