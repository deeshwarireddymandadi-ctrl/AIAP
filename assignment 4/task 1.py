def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND
    - It is either not divisible by 100 OR divisible by 400
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == "__main__":
    try:
        year = int(input("Enter a year to check if it's a leap year: ").strip())
        if year < 1:
            print("Please enter a positive year.")
        else:
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid integer year.")
# ...existing code...