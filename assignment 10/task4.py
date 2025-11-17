# ...existing code...
def sum_scores(scores):
    """Return the sum of scores."""
    return sum(scores)
def average_score(scores):
    """Return the average of scores (raises ValueError if empty)."""
    if not scores:
        raise ValueError("No scores provided.")
    return sum_scores(scores) / len(scores)
def max_score(scores):
    """Return the highest score (raises ValueError if empty)."""
    if not scores:
        raise ValueError("No scores provided.")
    return max(scores)
def min_score(scores):
    """Return the lowest score (raises ValueError if empty)."""
    if not scores:
        raise ValueError("No scores provided.")
    return min(scores)
def process_scores(scores):
    """Compute and return average, highest and lowest as a tuple."""
    return average_score(scores), max_score(scores), min_score(scores)
def parse_scores(input_str):
    """Parse a comma-separated string into a list of floats."""
    parts = [p.strip() for p in input_str.split(",") if p.strip() != ""]
    if not parts:
        return []
    return [float(p) for p in parts]
def main():
    print("=== Score Processor ===")
    raw = input("Enter scores (comma-separated): ").strip()
    try:
        scores = parse_scores(raw)
        if not scores:
            print("No scores entered.")
            return
        avg, high, low = process_scores(scores)
        print(f"Average: {avg:.2f}")
        print(f"Highest: {high}")
        print(f"Lowest: {low}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Error: Please enter numeric scores separated by commas.")
if __name__ == "__main__":
    main()
# ...existing code...