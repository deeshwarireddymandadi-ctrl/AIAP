def find_common(a, b):
    """Find common elements between two lists using set intersection."""
    return list(set(a) & set(b))
def find_common_preserving_order(a, b):
    """Find common elements while preserving order from list 'a'."""
    b_set = set(b)
    return [item for item in a if item in b_set]
def main():
    """Get user input and find common elements."""
    print("=== Find Common Elements ===\n")
    try:
        # Get first list
        input_a = input("Enter list A (comma-separated): ").strip()
        list_a = [x.strip() for x in input_a.split(",")]
        # Get second list
        input_b = input("Enter list B (comma-separated): ").strip()
        list_b = [x.strip() for x in input_b.split(",")]
        # Find common elements
        common = find_common_preserving_order(list_a, list_b)
        print(f"\nList A: {list_a}")
        print(f"List B: {list_b}")
        print(f"Common elements: {common}")
        print(f"Count: {len(common)}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()