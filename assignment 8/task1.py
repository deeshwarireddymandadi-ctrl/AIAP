def is_valid_email(email: str) -> bool:
    """
    Validate email address based on specific requirements.
    
    Requirements:
    - Must contain @ and . characters
    - Must not start or end with special characters
    - Should not allow multiple @
    
    Args:
        email: Email string to validate
        
    Returns:
        True if valid, False otherwise
    """
    email = email.strip()
    
    # Check if email is empty
    if not email:
        return False
    
    # Check if email contains exactly one @
    if email.count("@") != 1:
        return False
    
    # Check if email contains at least one .
    if "." not in email:
        return False
    
    # Split into local and domain parts
    local, domain = email.split("@")
    
    # Check if local part is empty
    if not local or not domain:
        return False
    
    # Check if starts with special characters
    if local[0] in ".-_":
        return False
    
    # Check if ends with special characters
    if local[-1] in ".-_" or domain[-1] in ".-_":
        return False
    
    # Check if domain has at least one dot
    if "." not in domain:
        return False
    
    # Check if domain parts are valid
    domain_parts = domain.split(".")
    if len(domain_parts) < 2:
        return False
    
    # Check if any domain part is empty
    for part in domain_parts:
        if not part:
            return False
    
    return True

def run_tests():
    """Run test cases for is_valid_email function"""
    test_cases = [
        # Valid emails
        ("user@example.com", True, "Basic valid email"),
        ("john.doe@company.co.uk", True, "Valid email with dots in local part"),
        ("test_email@domain.org", True, "Valid email with underscore"),
        ("a@b.c", True, "Minimal valid email"),
        
        # Invalid: missing @ or .
        ("userexample.com", False, "Missing @ symbol"),
        ("user@examplecom", False, "Missing . in domain"),
        ("user.example.com", False, "Missing @ symbol"),
        
        # Invalid: multiple @
        ("user@@example.com", False, "Multiple @ symbols"),
        ("user@domain@example.com", False, "Multiple @ symbols"),
        
        # Invalid: starts with special characters
        (".user@example.com", False, "Starts with dot"),
        ("-user@example.com", False, "Starts with dash"),
        ("_user@example.com", False, "Starts with underscore"),
        
        # Invalid: ends with special characters
        ("user.@example.com", False, "Local part ends with dot"),
        ("user-@example.com", False, "Local part ends with dash"),
        ("user_@example.com", False, "Local part ends with underscore"),
        ("user@example.com.", False, "Domain ends with dot"),
        ("user@example.com-", False, "Domain ends with dash"),
        
        # Invalid: empty parts
        ("@example.com", False, "Empty local part"),
        ("user@.com", False, "Empty domain first part"),
        ("user@example.", False, "Empty domain extension"),
        
        # Invalid: edge cases
        ("", False, "Empty string"),
        ("user", False, "No @ or domain"),
        ("@", False, "Only @ symbol"),
        ("user@", False, "Missing domain"),
        ("@example.com", False, "Missing local part"),
    ]
    
    print("Email Validator Test Cases")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for email, expected, description in test_cases:
        result = is_valid_email(email)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"{status} | Email: '{email}'")
        print(f"       Expected: {expected}, Got: {result}")
        print(f"       Description: {description}")
        print()
    
    print("=" * 70)
    print(f"Test Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    return failed == 0

if __name__ == "__main__":
    try:
        choice = input("1. Run test cases\n2. Validate single email\nEnter choice (1-2): ").strip()
        
        if choice == "1":
            success = run_tests()
            if success:
                print("\n✓ All tests passed!")
            else:
                print("\n✗ Some tests failed!")
                
        elif choice == "2":
            email = input("Enter email address to validate: ").strip()
            if is_valid_email(email):
                print(f"✓ '{email}' is a valid email address")
            else:
                print(f"✗ '{email}' is NOT a valid email address")
        else:
            print("Invalid choice!")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")