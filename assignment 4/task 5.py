def count_lines(filename: str) -> int:
    """
    Count the number of lines in a text file.
    
    Examples:
        count_lines("sample1.txt") -> 5    # File with 5 lines
        count_lines("empty.txt") -> 0      # Empty file
        count_lines("single.txt") -> 1     # File with one line
    
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")

if __name__ == "__main__":
    try:
        filename = input("Enter the path to your text file: ").strip()
        num_lines = count_lines(filename)
        print(f"Number of lines in {filename}: {num_lines}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")