"""
Test the dog age validation function.
"""

import sys
import os

# Add the server directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validation import validate_dog_age, is_valid_dog_age

def test_validate_dog_age():
    """Test the validate_dog_age function with various inputs."""
    
    print("Testing dog age validation...")
    
    # Test valid ages
    valid_ages = [0, 1, 5, 10, 15, 20, 0.5, 19.9]
    
    print("\n✅ Testing valid ages:")
    for age in valid_ages:
        try:
            result = validate_dog_age(age)
            print(f"  Age {age} -> {result} ✓")
        except Exception as e:
            print(f"  Age {age} -> ERROR: {e} ✗")
    
    # Test invalid ages
    invalid_ages = [-1, -5, 21, 25, 100]
    
    print("\n❌ Testing invalid ages (should raise errors):")
    for age in invalid_ages:
        try:
            result = validate_dog_age(age)
            print(f"  Age {age} -> {result} ✗ (Should have failed!)")
        except ValueError as e:
            print(f"  Age {age} -> ERROR: {e} ✓")
        except Exception as e:
            print(f"  Age {age} -> UNEXPECTED ERROR: {e} ?")
    
    # Test invalid types
    invalid_types = [None, "5", "old", [5], {"age": 5}]
    
    print("\n🚫 Testing invalid types (should raise errors):")
    for age in invalid_types:
        try:
            result = validate_dog_age(age)
            print(f"  Age {age} -> {result} ✗ (Should have failed!)")
        except (ValueError, TypeError) as e:
            print(f"  Age {age} -> ERROR: {e} ✓")
        except Exception as e:
            print(f"  Age {age} -> UNEXPECTED ERROR: {e} ?")
    
    # Test the is_valid_dog_age helper function
    print("\n🔍 Testing is_valid_dog_age helper function:")
    test_cases = [
        (5, True),
        (20, True),
        (0, True),
        (-1, False),
        (21, False),
        ("5", False),
        (None, False)
    ]
    
    for age, expected in test_cases:
        result = is_valid_dog_age(age)
        status = "✓" if result == expected else "✗"
        print(f"  is_valid_dog_age({age}) -> {result} (expected {expected}) {status}")

if __name__ == "__main__":
    test_validate_dog_age()
