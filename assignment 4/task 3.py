def format_name(first: str, last: str) -> str:
    """
    Format full name as 'Last, First'
    
    Examples:
        format_name('John', 'Smith') -> 'Smith, John'
        format_name('Mary', 'Jones') -> 'Jones, Mary'
        format_name('Bob', 'Wilson') -> 'Wilson, Bob'
    """
    return f"{last}, {first}"

if __name__ == "__main__":
    try:
        first = input("Enter first name: ").strip()
        last = input("Enter last name: ").strip()
        if not first or not last:
            print("Both first and last names are required.")
        else:
            formatted = format_name(first, last)
            print(f"Formatted name: {formatted}")
    except Exception as e:
        print(f"An error occurred: {e}")