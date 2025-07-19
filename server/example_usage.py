"""
Example usage of dog age validation functions.
"""

from utils.validation import validate_dog_age, is_valid_dog_age

def example_usage():
    """Demonstrate how to use the dog age validation functions."""
    
    print("=== Dog Age Validation Examples ===\n")
    
    # Example 1: Using validate_dog_age (throws exceptions)
    print("1. Using validate_dog_age() function:")
    print("   This function validates and returns the age, or throws an exception")
    
    ages_to_test = [5, 15, 20, -1, 25, "5", None]
    
    for age in ages_to_test:
        try:
            validated_age = validate_dog_age(age)
            print(f"   ✅ Age {age} -> Valid: {validated_age}")
        except (ValueError, TypeError) as e:
            print(f"   ❌ Age {age} -> Invalid: {e}")
    
    print("\n" + "-"*50 + "\n")
    
    # Example 2: Using is_valid_dog_age (returns boolean)
    print("2. Using is_valid_dog_age() function:")
    print("   This function checks validity without throwing exceptions")
    
    for age in ages_to_test:
        is_valid = is_valid_dog_age(age)
        status = "✅ Valid" if is_valid else "❌ Invalid"
        print(f"   {status}: Age {age}")
    
    print("\n" + "-"*50 + "\n")
    
    # Example 3: Practical usage in a form validation scenario
    print("3. Practical example - Form validation:")
    
    def process_dog_registration(name, age_input):
        """Example function that might be used in a web form."""
        try:
            # Validate the age
            validated_age = validate_dog_age(age_input)
            print(f"   ✅ Dog '{name}' registered successfully with age {validated_age}")
            return True
        except (ValueError, TypeError) as e:
            print(f"   ❌ Registration failed for '{name}': {e}")
            return False
    
    # Test cases for the registration function
    test_dogs = [
        ("Buddy", 5),
        ("Max", 0),
        ("Luna", 20),
        ("Charlie", -2),
        ("Bella", 25),
        ("Rocky", "three"),
    ]
    
    for name, age in test_dogs:
        process_dog_registration(name, age)

if __name__ == "__main__":
    example_usage()
