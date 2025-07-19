"""
Validation utilities for the pets application.
"""

def validate_dog_age(age):
    """
    Validate dog age to ensure it's between 0 and 20 years.
    
    Args:
        age (int or float): The age to validate
        
    Returns:
        int: The validated age
        
    Raises:
        ValueError: If age is outside the valid range (0-20) or not a valid number
        TypeError: If age is not a number type
    """
    if age is None:
        raise ValueError("Age cannot be None")
    
    # Check for boolean values first (they're technically int/float in Python)
    if isinstance(age, bool):
        raise TypeError("Age must be a number (int or float)")
    
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number (int or float)")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 20:
        raise ValueError("Age cannot be greater than 20 years")
    
    return int(age)


def is_valid_dog_age(age):
    """
    Check if a dog age is valid without raising an exception.
    
    Args:
        age: The age to check
        
    Returns:
        bool: True if age is valid, False otherwise
    """
    try:
        validate_dog_age(age)
        return True
    except (ValueError, TypeError):
        return False
