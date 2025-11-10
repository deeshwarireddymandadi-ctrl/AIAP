def classify_age(age: int) -> str:
    """
    Classify a person's age group using nested conditionals.
    Returns appropriate category and any special notes.
    """
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        if age <= 2:
            return "Infant"
        elif age <= 5:
            return "Toddler"
        else:
            return "Child"
    elif age <= 19:
        if age <= 15:
            return "Early Teen"
        else:
            return "Late Teen"
    elif age <= 65:
        if age <= 35:
            return "Young Adult"
        elif age <= 50:
            return "Adult"
        else:
            return "Senior Adult"
    else:
        if age <= 80:
            return "Senior Citizen"
        else:
            return "Elder"

def get_age_status(age: int) -> str:
    """Alternative classification using match-case (Python 3.10+)"""
    match age:
        case _ if age < 0:
            return "Invalid age"
        case _ if age <= 2:
            return "Infant"
        case _ if age <= 12:
            return "Child"
        case _ if age <= 19:
            return "Teen"
        case _ if age <= 65:
            return "Adult"
        case _:
            return "Senior"

if __name__ == "__main__":
    try:
        age_input = input("Enter age: ").strip()
        age = int(age_input)
        
        # Using nested if-elif-else
        category = classify_age(age)
        print(f"\nDetailed classification: {category}")
        
        # Using match-case (alternative)
        basic_status = get_age_status(age)
        print(f"Basic classification: {basic_status}")
        
        # Additional conditional checks
        if age >= 0:
            if age >= 18:
                print("Status: Adult (Legal)")
                if age >= 21:
                    print("- Can purchase alcohol (US)")
                if age >= 25:
                    print("- Can rent a car")
            else:
                print("Status: Minor")
                years_to_18 = 18 - age
                print(f"- Years until legal adult: {years_to_18}")
                
    except ValueError:
        print("Please enter a valid integer for age.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")