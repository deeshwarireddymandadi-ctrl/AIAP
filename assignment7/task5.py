def get_list_item(numbers: list, index: int) -> str:
    """
    Safely access a list item with error handling.
    
    Args:
        numbers: List to access
        index: Desired index position
        
    Returns:
        String describing the result or error
    """
    try:
        return f"Value at index {index}: {numbers[index]}"
    except IndexError:
        return f"Error: Index {index} is out of range. Valid indices are 0 to {len(numbers)-1}"

if __name__ == "__main__":
    numbers = [1, 2, 3]
    
    try:
        index = int(input(f"Enter an index to access (list has {len(numbers)} items): "))
        result = get_list_item(numbers, index)
        print(result)
        
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")