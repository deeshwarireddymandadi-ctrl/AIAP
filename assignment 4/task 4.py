def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a given string.
    Case-insensitive.
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == "__main__":
    try:
        text = input("Enter a string to count vowels: ").strip()
        count = count_vowels(text)
        print(f"Number of vowels: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")