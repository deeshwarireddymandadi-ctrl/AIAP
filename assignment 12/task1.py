def linear_search(data_list, target_value):
    """
    Searches for a target_value in the data_list using the Linear Search algorithm.

    Linear search checks every element in the list sequentially until the target
    is found or the end of the list is reached.

    Args:
        data_list (list): The list of elements to search through.
        target_value: The value being searched for.

    Returns:
        int: The index of the target_value if found, otherwise returns -1.
    """
    # 1. Iterate through the list using the index
    for index in range(len(data_list)):
        # 2. Check if the current element matches the target
        if data_list[index] == target_value:
            # 3. If a match is found, return the current index
            return index

    # 4. If the loop completes without finding the target, return -1
    return -1

def get_list_input():
    """
    Prompts the user to enter a list of numbers, separated by commas.

    Returns:
        list: A list of integers derived from the user input.
    """
    while True:
        try:
            # Get the input string from the user
            input_str = input("Enter a list of numbers (e.g., 1,5,12,8,30): ")

            # Split the string by comma, remove whitespace, and convert to integers
            # This handles cases where the user might enter extra spaces
            data_list = [int(item.strip()) for item in input_str.split(',')]

            return data_list
        except ValueError:
            print("Invalid input. Please ensure all items are valid integers and are separated by commas.")

def get_target_input():
    """
    Prompts the user to enter the single value they want to search for.

    Returns:
        int: The integer target value.
    """
    while True:
        try:
            # Get the target value and convert it to an integer
            target = int(input("Enter the single number you want to search for: "))
            return target
        except ValueError:
            print("Invalid input. Please enter a single, valid integer.")

def main():
    """
    Main function to execute the linear search process.
    """
    print("\n--- Linear Search Program ---")

    # 1. Get the list from the user
    my_list = get_list_input()
    print(f"List to search: {my_list}")

    # 2. Get the target value from the user
    target = get_target_input()

    # 3. Perform the search
    index_found = linear_search(my_list, target)

    # 4. Display the results
    if index_found != -1:
        print(f"\nSUCCESS! The value {target} was found.")
        print(f"It is located at index: {index_found}")
    else:
        print(f"\nNOT FOUND. The value {target} is not present in the list.")

# This ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()