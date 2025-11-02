# ...existing code...

def find_largest(numbers: list[float]) -> float:
    """Return the largest number from numbers.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("empty list")
    return max(numbers)

if __name__ == "__main__":
    try:
        s = input("Enter numbers separated by spaces or commas: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nNo input provided.")
    else:
        if not s:
            print("No numbers provided.")
        else:
            # allow commas or spaces as separators
            tokens = s.replace(",", " ").split()
            try:
                nums = [float(t) for t in tokens]
            except ValueError:
                print("Invalid input: please enter only numeric values separated by spaces or commas.")
            else:
                try:
                    largest = find_largest(nums)
                except ValueError:
                    print("No numbers to evaluate.")
                else:
                    # print as int if it's an integer value
                    if largest.is_integer():
                        print(f"Largest number: {int(largest)}")
                    else:
                        print(f"Largest number: {largest}")
# ...existing code...