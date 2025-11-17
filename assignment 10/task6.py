# ...existing code...
def grade(score):
    """Return letter grade for a numeric score (0-100)."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def main():
    try:
        s = float(input("Enter score (0-100): ").strip())
    except ValueError:
        print("Invalid input: please enter a numeric score.")
        return
    try:
        print("Grade:", grade(s))
    except ValueError as e:
        print("Error:", e)
if __name__ == "__main__":
    main()
# ...existing code...