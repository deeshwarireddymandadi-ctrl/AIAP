# ...existing code...

def reverse_string(s: str) -> str:
    """Return the reversed version of s."""
    return s[::-1]

if __name__ == "__main__":
    try:
        s = input("Enter a string to reverse: ")
    except (EOFError, KeyboardInterrupt):
        print("\nNo input provided.")
    else:
        print(reverse_string(s))
# ...existing code...