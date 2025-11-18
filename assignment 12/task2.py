def get_user_list():
    """Prompts the user to enter a list of integers."""
    while True:
        try:
            # Get a comma-separated string of numbers
            input_str = input("Enter a list of integers, separated by commas (e.g., 5, 1, 4, 2, 8): ")
            # Convert the string into a list of integers
            data_list = [int(x.strip()) for x in input_str.split(',')]
            return data_list
        except ValueError:
            print("Invalid input. Please ensure all entries are integers separated by commas.")

def bubble_sort(arr):
    """
    Sorts an array using the optimized Bubble Sort algorithm in ascending order.
    Returns the sorted array.
    """
    n = len(arr)
    # Outer loop for number of passes (n-1 passes are sufficient)
    for i in range(n - 1):
        # Flag to optimize: if no two elements are swapped in inner loop, array is sorted
        swapped = False
        
        # Inner loop for comparisons and swaps
        # The last 'i' elements are already in place, so we don't check them.
        for j in range(0, n - i - 1):
            # Compare the adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap them if the first is greater than the second (for ascending order)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then the array is sorted
        if not swapped:
            break
            
    return arr

# --- Main execution block ---

# 1. Get user input
unsorted_list = get_user_list()
print("\nOriginal List:", unsorted_list)

# Create a copy to sort, keeping the original for comparison
list_to_sort = list(unsorted_list) 

# 2. Implement Bubble Sort
sorted_list = bubble_sort(list_to_sort)

# 3. Check and print sorted output
print("Sorted Output:", sorted_list)

# 4. Simple Verification (Optional but good practice)
is_correctly_sorted = True
for i in range(len(sorted_list) - 1):
    if sorted_list[i] > sorted_list[i+1]:
        is_correctly_sorted = False
        break

print("-" * 30)
if is_correctly_sorted:
    print("✅ Verification: The output is correctly sorted in ascending order.")
else:
    print("❌ Verification: There was an issue with the sort, the output is NOT fully sorted.")