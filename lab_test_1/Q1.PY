import timeit
import random
from typing import List, Any, Optional

# Define the size of the list for performance testing
LIST_SIZE = 1_000_000  # One million elements
# Number of times to run the test for better average results
REPEAT_COUNT = 5

# --- 1. AI-Suggested Alternative Implementations ---
# Based on common Python patterns and efficiency analyses.

def reverse_method_1_inplace(data: List[Any]) -> List[Any]:
    """
    Method 1: The built-in list.reverse() method.
    
    - Reverses the list in place (mutates the original list).
    - Time Complexity: O(n)
    - Space Complexity: O(1) (most memory efficient for the operation itself)
    - NOTE: We return the modified copy to showcase the result without mutating the input 'data'
    """
    list_copy = data[:] 
    list_copy.reverse()
    return list_copy

def reverse_method_2_slicing(data: List[Any]) -> List[Any]:
    """
    Method 2: The Slicing Technique [::-1].
    
    - Creates and returns a new reversed list (does not mutate the original).
    - Time Complexity: O(n)
    - Space Complexity: O(n) (requires memory for the new list)
    """
    return data[::-1]

def reverse_method_3_reversed_function(data: List[Any]) -> List[Any]:
    """
    Method 3: Using the built-in reversed() function and converting to a list.
    
    - Creates an iterator (reversed()) then materializes it as a new list.
    - Time Complexity: O(n)
    - Space Complexity: O(n) (requires memory for the new list)
    """
    return list(reversed(data))

def reverse_method_4_manual_swap(data: List[Any]) -> List[Any]:
    """
    Method 4: Manual Swapping (In-place algorithm simulation).
    
    - Reverses the list in place by swapping elements from opposite ends.
    - Useful for understanding the underlying algorithm, but generally slower than built-ins.
    - Time Complexity: O(n)
    - Space Complexity: O(1) for the core algorithm (O(n) for the initial copy).
    """
    list_copy = data[:] # Work on a copy
    n = len(list_copy)
    for i in range(n // 2):
        # Swap elements: list[i] with list[n - 1 - i]
        list_copy[i], list_copy[n - 1 - i] = list_copy[n - 1 - i], list_copy[i]
    return list_copy

# --- 2. User Input Function ---

def get_user_list() -> Optional[List[Any]]:
    """
    Prompts the user to enter a list of elements and returns a processed list.
    """
    print("\n--- User Input Demonstration ---")
    user_input = input("Enter list elements separated by commas (e.g., 1, hello, 3.14, 4): ")
    
    if not user_input.strip():
        print("No input provided. Skipping demonstration.")
        return None
        
    # Split by comma, strip whitespace, and return as a list of strings
    # Note: We keep elements as strings for simplicity, as type conversion is complex.
    input_list = [item.strip() for item in user_input.split(',')]
    return input_list

# --- 3. Performance Test Function (for large list) ---

def run_tests():
    """
    Initializes a large list and runs performance tests on all methods.
    """
    print(f"\n" + "="*70)
    print(f"--- Comprehensive Performance Test ---")
    print(f"Goal: Compare C-optimized built-ins vs. Python manual implementation.")
    print(f"List Size: {LIST_SIZE:,} integers")
    print(f"Test Repetitions (per method): {REPEAT_COUNT}\n")

    # 1. Setup the large input list once
    initial_list = list(range(LIST_SIZE))
    # We shuffle it to ensure the list is not already sorted (which might skew results)
    random.shuffle(initial_list) 

    # 2. Define methods to test
    # Note: For timing, we must ensure the list is copied inside the setup for in-place methods
    # so that the reversal happens on a fresh list every time.
    methods = [
        # Note: list.reverse() is timed on a copy of initial_list (test_list)
        ("1. list.reverse() (In-place)", "test_list.reverse()", "test_list = initial_list[:]"),
        ("2. Slicing [::-1] (New List)", "initial_list[::-1]", "pass"), # Slicing is fastest
        ("3. list(reversed()) (New List)", "list(reversed(initial_list))", "pass"),
        # We time the function wrapper which performs the swapping on its own copy
        ("4. Manual Swap Loop (In-place)", "reverse_method_4_manual_swap(test_list)", "test_list = initial_list[:]"),
    ]

    results = {}

    # 3. Run timeit for each method
    for name, statement, setup in methods:
        # Define the context for timeit
        context = {
            'initial_list': initial_list, 
            'reverse_method_4_manual_swap': reverse_method_4_manual_swap,
        }

        # Time the execution of the statement
        times = timeit.repeat(
            stmt=statement, 
            setup=setup,
            repeat=REPEAT_COUNT, 
            number=1, # Execute the statement 1 time per repeat
            globals=context
        )
        
        # Calculate the average time (in seconds)
        average_time = sum(times) / REPEAT_COUNT
        results[name] = average_time

    # 4. Display Results
    print(f"{'Method':<30} | {'Avg. Time (s)':<15} | {'Notes':<10}")
    print("-" * 60)

    # Sort results by time (fastest first)
    sorted_results = sorted(results.items(), key=lambda item: item[1])
    
    for name, avg_time in sorted_results:
        clean_name = name.split("(", 1)[0].strip() # Clean up method name for printing

        # Determine the type of operation for clarity
        if "In-place" in name:
            op_notes = "In-place (O(1) space)"
        elif "Slicing" in name:
            op_notes = "New List (O(n) space)"
        else:
            op_notes = "New List (O(n) space)"

        print(f"{clean_name:<30} | {avg_time:^15.6f} | {op_notes:<20}")

    print("\n--- Summary ---")
    fastest_name, fastest_time = sorted_results[0]
    print(f"The fastest method was: {fastest_name.split('(', 1)[0].strip()}")
    print("The built-in methods (list.reverse() and slicing) are almost always superior due to C implementation.\n")


# --- 4. Main Execution Block ---

if __name__ == "__main__":
    
    user_list = get_user_list()
    
    if user_list:
        print(f"\nOriginal List (from user input): {user_list}")
        
        # Method 1: list.reverse() (In-place, but run on a copy for demo)
        reversed_1 = reverse_method_1_inplace(user_list)
        print(f"1. list.reverse() Result: {reversed_1}")
        
        # Method 2: Slicing [::-1] (New List)
        reversed_2 = reverse_method_2_slicing(user_list)
        print(f"2. Slicing [::-1] Result: {reversed_2}")

        # Method 3: list(reversed()) (New List)
        reversed_3 = reverse_method_3_reversed_function(user_list)
        print(f"3. list(reversed()) Result: {reversed_3}")
        
        # Method 4: Manual Swap (In-place algorithm simulation)
        reversed_4 = reverse_method_4_manual_swap(user_list)
        print(f"4. Manual Swap Result: {reversed_4}")

        print(f"\nOriginal List remains: {user_list}")
    else:
        print("Skipping user list demonstration.")


    run_tests()