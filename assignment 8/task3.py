import re

def is_sentence_palindrome(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome, ignoring case, spaces, and punctuation.
    
    A palindrome reads the same forwards and backwards when ignoring non-alphanumeric
    characters and case differences.
    
    Args:
        sentence: String to check if it's a palindrome
        
    Returns:
        True if sentence is a palindrome, False otherwise
        
    Raises:
        TypeError: If input is not a string
    """
    # Validate input type
    if not isinstance(sentence, str):
        raise TypeError(f"Input must be a string, not {type(sentence).__name__}")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    
    # Handle empty or single character strings
    if len(cleaned) <= 1:
        return True
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]

def run_tests():
    """Run comprehensive test cases for is_sentence_palindrome function"""
    
    test_cases = [
        # Classic palindromes
        ("A man, a plan, a canal: Panama", True, "Famous Panama Canal palindrome"),
        ("race car", True, "Simple race car palindrome"),
        ("madam", True, "Classic madam palindrome"),
        ("Was it a car or a cat I saw?", True, "Question palindrome"),
        
        # Palindromes with punctuation and spaces
        ("Able was I ere I saw Elba", True, "Able was I ere I saw Elba"),
        ("A Santa at NASA", True, "NASA palindrome"),
        ("Do geese see God?", True, "Do geese see God palindrome"),
        ("Never odd or even", True, "Never odd or even palindrome"),
        ("No 'x' in Nixon", True, "Nixon palindrome with quotes"),
        
        # Palindromes with mixed case and punctuation
        ("Madam, I'm Adam", True, "Madam I'm Adam"),
        ("Never a foot too far, even.", True, "Never a foot too far, even"),
        ("Mr. Owl ate my metal worm", True, "Owl palindrome"),
        ("A1B2B1A", True, "Alphanumeric palindrome"),
        
        # Single and double character cases
        ("a", True, "Single character"),
        ("A", True, "Single uppercase character"),
        ("aa", True, "Two same characters"),
        ("ab", False, "Two different characters"),
        ("A-A", True, "Two same with punctuation"),
        
        # Empty and whitespace
        ("", True, "Empty string"),
        ("   ", True, "Only spaces"),
        ("!!!", True, "Only punctuation"),
        ("   A   ", True, "Single char with spaces"),
        
        # Numbers included
        ("12321", True, "Numeric palindrome"),
        ("12345", False, "Numeric non-palindrome"),
        ("A1B1A", True, "Alphanumeric palindrome"),
        ("1a2b2a1", True, "Complex alphanumeric"),
        
        # Common non-palindromes
        ("hello", False, "Simple non-palindrome"),
        ("Hello World", False, "Phrase non-palindrome"),
        ("Python", False, "Python non-palindrome"),
        ("The quick brown fox", False, "Sentence non-palindrome"),
        ("banana", False, "Banana non-palindrome"),
        
        # Edge cases with punctuation
        ("A.B.A", True, "Punctuation between letters"),
        ("A-B-C-B-A", True, "Dashes between letters"),
        ("A!@#$%B!@#$%A", True, "Multiple punctuation types"),
        ("!!!A!!!B!!!A!!!", True, "Punctuation everywhere"),
        
        # Case sensitivity tests
        ("AbA", True, "Mixed case palindrome"),
        ("AbC", False, "Mixed case non-palindrome"),
        ("AaBbCcBbAa", True, "Complex mixed case"),
        
        # More complex examples
        ("Madam, I'm Adam!", True, "Madam complex"),
        ("Was it a rat I saw?", True, "Rat palindrome"),
        ("Go hang a salami, I'm a lasagna hog", True, "Lasagna hog palindrome"),
        ("Able, was I ere I saw Elba", True, "Elba palindrome"),
        ("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.", True, "Long complex palindrome"),
    ]
    
    error_cases = [
        (123, TypeError, "Integer input"),
        (12.34, TypeError, "Float input"),
        (None, TypeError, "None input"),
        (["a", "b"], TypeError, "List input"),
        ({"text": "hello"}, TypeError, "Dictionary input"),
    ]
    
    print("=" * 90)
    print("IS_SENTENCE_PALINDROME TEST CASES")
    print("=" * 90)
    
    passed = 0
    failed = 0
    
    # Test valid cases
    print("\nVALID INPUT TESTS:")
    print("-" * 90)
    
    for sentence, expected, description in test_cases:
        try:
            result = is_sentence_palindrome(sentence)
            status = "✓ PASS" if result == expected else "✗ FAIL"
            
            if result == expected:
                passed += 1
            else:
                failed += 1
            
            display_text = sentence if len(sentence) <= 50 else sentence[:47] + "..."
            print(f"{status} | Input: '{display_text}'")
            print(f"       Expected: {expected}, Got: {result}")
            print(f"       Description: {description}")
            
        except Exception as e:
            print(f"✗ FAIL | Input: '{sentence}'")
            print(f"        Unexpected exception: {e}")
            failed += 1
        print()
    
    # Test error cases
    print("\nINVALID INPUT TESTS (Error Handling):")
    print("-" * 90)
    
    for value, expected_error, description in error_cases:
        try:
            result = is_sentence_palindrome(value)
            print(f"✗ FAIL | Value: {value} | Expected {expected_error.__name__}, but got result: {result}")
            print(f"        Description: {description}")
            failed += 1
        except expected_error as e:
            print(f"✓ PASS | Value: {value} | Raised {expected_error.__name__}")
            print(f"        Description: {description}")
            passed += 1
        except Exception as e:
            print(f"✗ FAIL | Value: {value} | Expected {expected_error.__name__}, got {type(e).__name__}: {e}")
            print(f"        Description: {description}")
            failed += 1
        print()
    
    print("=" * 90)
    total = passed + failed
    print(f"TEST SUMMARY: {passed}/{total} passed, {failed}/{total} failed")
    print("=" * 90)
    return failed == 0

if __name__ == "__main__":
    try:
        choice = input("1. Run all test cases\n2. Check single sentence\nEnter choice (1-2): ").strip()
        
        if choice == "1":
            success = run_tests()
            if success:
                print("\n✓ All tests passed!")
            else:
                print("\n✗ Some tests failed!")
                
        elif choice == "2":
            try:
                sentence = input("Enter a sentence to check if it's a palindrome: ").strip()
                result = is_sentence_palindrome(sentence)
                status = "✓ IS" if result else "✗ IS NOT"
                print(f"\n{status} a palindrome: '{sentence}'")
            except TypeError as e:
                print(f"\n✗ Error: {e}")
        else:
            print("Invalid choice!")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")