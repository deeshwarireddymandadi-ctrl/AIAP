def print_multiples(number: int, count: int = 10) -> None:
    """
    Print the first 'count' multiples of the given number.
    
    Args:
        number: The number to find multiples of
        count: Number of multiples to print (default: 10)
    """
    print(f"First {count} multiples of {number}:")
    for i in range(1, count + 1):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")

if __name__ == "__main__":
    try:
        num = input("Enter a number to find its multiples: ").strip()
        number = int(num)
        
        # Optional: allow user to specify how many multiples
        count_input = input("How many multiples to show? [10]: ").strip()
        count = int(count_input) if count_input else 10
        
        if count <= 0:
            print("Please enter a positive count.")
        else:
            print_multiples(number, count)
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")