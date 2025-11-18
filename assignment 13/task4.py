import sys

def get_list_input(prompt):
    """
    Safely gets a string of numbers from the user and converts it to a list of integers.
    """
    while True:
        try:
            input_str = input(prompt).strip()
            if not input_str:
                return []
            
            # Attempt to split the string by commas and convert to integers/floats
            numbers = [float(x.strip()) for x in input_str.split(',')]
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas (e.g., 1, 2, 3.5, 4).")
        except EOFError:
            print("\nInput cancelled. Exiting.")
            sys.exit(0)

def calculate_squares_refactored(nums):
    """
    Refactored, efficient function to calculate squares using a list comprehension.
    
    The original inefficient loop:
    squares = []
    for i in nums:
        squares.append(i * i)
    
    is replaced by:
    """
    # List Comprehension: This is the idiomatic, fast, and concise Python way
    # to create a new list based on an existing iterable.
    squares = [i * i for i in nums]
    return squares

def main():
    """Handles user input and demonstrates the refactored function."""
    print("--- Efficient List Squarer ---")
    
    # 1. Provide a default list to demonstrate the initial functionality
    default_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("\nDefault list provided in the original code:")
    print(f"Input: {default_nums}")
    default_squares = calculate_squares_refactored(default_nums)
    print(f"Output (List Comprehension): {default_squares}")
    
    print("\n==================================")
    
    # 2. Ask for user input
    print("Now, enter your own list of numbers.")
    user_nums = get_list_input("Enter numbers separated by commas (e.g., 10, 20, 30): ")

    if not user_nums:
        print("No numbers entered. Exiting.")
        return

    # 3. Calculate and display the refactored result
    user_squares = calculate_squares_refactored(user_nums)
    
    print("\n--- Refactored Result ---")
    print(f"Your Input List: {user_nums}")
    print(f"Squared List: {user_squares}")
    print("This was generated using a fast and readable list comprehension.")

if __name__ == "__main__":
    main()