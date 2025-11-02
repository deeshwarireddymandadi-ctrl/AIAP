# ...existing code...

def is_palindrome(s: str) -> bool:
    """Check if the given string s is a palindrome."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    try:
        s = input("Enter a string to check if it's a palindrome: ")
        if is_palindrome(s):
            print(f'"{s}" is a palindrome.')
        else:
            print(f'"{s}" is not a palindrome.')
    except Exception as e:
        print(f"An error occurred: {e}")
# ...existing code...