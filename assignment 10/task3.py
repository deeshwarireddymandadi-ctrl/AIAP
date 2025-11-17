class Employee:
    """Represents an employee with salary management capabilities."""   
    def __init__(self, name, salary):
        """Initialize employee with name and salary.        
        Args:
            name (str): Employee's full name
            salary (float): Employee's base salary
        """
        self._name = name
        self._salary = salary
    @property
    def name(self):
        """Get employee name."""
        return self._name
    @property
    def salary(self):
        """Get current salary."""
        return self._salary
    def apply_raise(self, percentage):
        """Apply a percentage-based salary increase.
        Args:
            percentage (float): Percentage increase (e.g., 10 for 10%)
        Raises:
            ValueError: If percentage is negative
        """
        if percentage < 0:
            raise ValueError("Percentage increase cannot be negative.")
        self._salary += self._salary * (percentage / 100)
    def display_info(self):
        """Display employee information."""
        print(f"Employee: {self._name}")
        print(f"Salary: ${self._salary:.2f}")
    def __str__(self):
        """String representation of employee."""
        return f"{self._name} - ${self._salary:.2f}"
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Employee(name='{self._name}', salary={self._salary})"
def main():
    """Get user input and manage employee data."""
    print("=== Employee Salary Manager ===\n")
    try:
        # Get employee details
        name = input("Enter employee name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        salary = float(input("Enter base salary ($): "))
        if salary < 0:
            print("Error: Salary cannot be negative.")
            return
        # Create employee
        employee = Employee(name, salary)
        print(f"\nEmployee created: {employee}")
        # Apply raise
        while True:
            raise_percent = float(input("\nEnter raise percentage (or -1 to exit): "))
            if raise_percent == -1:
                break
            employee.apply_raise(raise_percent)
            print(f"New salary after {raise_percent}% raise: ${employee.salary:.2f}")        
        # Display final info
        print("\n=== Final Employee Info ===")
        employee.display_info()        
    except ValueError as e:
        print(f"Error: Please enter valid input. {e}")
if __name__ == "__main__":
    main()