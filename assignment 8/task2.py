def assign_grade(score) -> str:
    """
    Assign a letter grade based on numeric score.
    
    Grade scale:
    - 90-100: A
    - 80-89: B
    - 70-79: C
    - 60-69: D
    - Below 60: F
    
    Args:
        score: Numeric score (0-100)
        
    Returns:
        Letter grade (A, B, C, D, or F)
        
    Raises:
        TypeError: If score is not a number
        ValueError: If score is outside valid range (0-100)
    """
    # Validate input type
    if not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, not {type(score).__name__}")
    
    # Check for NaN or infinity
    if isinstance(score, float) and (score != score or score == float('inf') or score == float('-inf')):
        raise ValueError("Score cannot be NaN or infinity")
    
    # Validate score range
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    
    # Assign grade
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

def run_tests():
    """Run comprehensive test cases for assign_grade function"""
    
    test_cases = [
        # Valid: Perfect and failing scores
        (100, "A", "Perfect score"),
        (0, "F", "Lowest passing score"),
        
        # Valid: Boundary values - Grade A
        (90, "A", "Lower boundary of A"),
        (99, "A", "Upper boundary of A (just below 100)"),
        
        # Valid: Boundary values - Grade B
        (89, "B", "Upper boundary of B"),
        (80, "B", "Lower boundary of B"),
        
        # Valid: Boundary values - Grade C
        (79, "C", "Upper boundary of C"),
        (70, "C", "Lower boundary of C"),
        
        # Valid: Boundary values - Grade D
        (69, "D", "Upper boundary of D"),
        (60, "D", "Lower boundary of D"),
        
        # Valid: Below D (F)
        (59, "F", "Just below D"),
        (1, "F", "Minimal failing score"),
        
        # Valid: Mid-range scores
        (95, "A", "Mid-range A"),
        (85, "B", "Mid-range B"),
        (75, "C", "Mid-range C"),
        (65, "D", "Mid-range D"),
        (45, "F", "Mid-range F"),
        
        # Valid: Float values
        (90.5, "A", "Float score in A range"),
        (80.1, "B", "Float score in B range"),
        (70.9, "C", "Float score in C range"),
        (60.0, "D", "Float score in D range"),
        (59.9, "F", "Float score in F range"),
    ]
    
    error_cases = [
        # Invalid: Out of range
        (-5, ValueError, "Negative score"),
        (-100, ValueError, "Large negative score"),
        (101, ValueError, "Score above 100"),
        (150, ValueError, "Score way above 100"),
        
        # Invalid: Wrong data types
        ("eighty", TypeError, "String input"),
        ("90", TypeError, "Numeric string"),
        (None, TypeError, "None value"),
        ([90], TypeError, "List input"),
        ({"score": 90}, TypeError, "Dictionary input"),
        
        # Invalid: Special float values
        (float('inf'), ValueError, "Positive infinity"),
        (float('-inf'), ValueError, "Negative infinity"),
        (float('nan'), ValueError, "NaN value"),
    ]
    
    print("=" * 80)
    print("ASSIGN_GRADE TEST CASES")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    # Test valid cases
    print("\nVALID INPUT TESTS:")
    print("-" * 80)
    
    for score, expected, description in test_cases:
        try:
            result = assign_grade(score)
            if result == expected:
                print(f"✓ PASS | Score: {score:>6} | Expected: {expected} | Got: {result}")
                print(f"        Description: {description}")
                passed += 1
            else:
                print(f"✗ FAIL | Score: {score:>6} | Expected: {expected} | Got: {result}")
                print(f"        Description: {description}")
                failed += 1
        except Exception as e:
            print(f"✗ FAIL | Score: {score:>6} | Unexpected exception: {e}")
            print(f"        Description: {description}")
            failed += 1
        print()
    
    # Test error cases
    print("\nINVALID INPUT TESTS (Error Handling):")
    print("-" * 80)
    
    for value, expected_error, description in error_cases:
        try:
            result = assign_grade(value)
            print(f"✗ FAIL | Value: {value} | Expected {expected_error.__name__}, but got result: {result}")
            print(f"        Description: {description}")
            failed += 1
        except expected_error as e:
            print(f"✓ PASS | Value: {value} | Raised {expected_error.__name__}: {e}")
            print(f"        Description: {description}")
            passed += 1
        except Exception as e:
            print(f"✗ FAIL | Value: {value} | Expected {expected_error.__name__}, got {type(e).__name__}: {e}")
            print(f"        Description: {description}")
            failed += 1
        print()
    
    print("=" * 80)
    total = passed + failed
    print(f"TEST SUMMARY: {passed}/{total} passed, {failed}/{total} failed")
    print("=" * 80)
    return failed == 0

if __name__ == "__main__":
    try:
        choice = input("1. Run all test cases\n2. Check grade for single score\nEnter choice (1-2): ").strip()
        
        if choice == "1":
            success = run_tests()
            if success:
                print("\n✓ All tests passed!")
            else:
                print("\n✗ Some tests failed!")
                
        elif choice == "2":
            try:
                score = float(input("Enter score (0-100): "))
                grade = assign_grade(score)
                print(f"\n✓ Score {score} → Grade: {grade}")
            except (ValueError, TypeError) as e:
                print(f"\n✗ Error: {e}")
        else:
            print("Invalid choice!")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")