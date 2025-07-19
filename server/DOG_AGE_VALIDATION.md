# Dog Age Validation Implementation

## Overview
I've created comprehensive dog age validation functionality for the pets-sample project. The validation ensures that dog ages are between 0 and 20 years, throwing appropriate errors for invalid values.

## Files Created/Modified

### 1. Modified: `/server/models/dog.py`
- Added `@validates('age')` decorator method to the `Dog` SQLAlchemy model
- Validates ages during database operations
- Ensures ages are numeric and within the 0-20 range
- Allows `None` values (nullable field)

### 2. Created: `/server/utils/validation.py`
- `validate_dog_age(age)`: Standalone validation function that throws exceptions
- `is_valid_dog_age(age)`: Helper function that returns boolean without exceptions
- Comprehensive error handling with descriptive messages

### 3. Created: `/server/test_dog_validation.py`
- Unit tests for the Dog model age validation
- Tests valid ages, invalid ages, and edge cases
- Uses unittest framework for systematic testing

### 4. Created: `/server/test_validation.py`
- Tests for the standalone validation functions
- Comprehensive test coverage with visual output
- Tests both validation functions and edge cases

### 5. Created: `/server/example_usage.py`
- Practical examples of how to use the validation functions
- Demonstrates both exception-based and boolean-based validation
- Shows real-world usage scenarios

## Validation Rules

### Valid Ages
- **Range**: 0 to 20 years (inclusive)
- **Types**: Integers and floats
- **Special**: `None` is allowed (for nullable database fields)

### Invalid Ages
- **Negative values**: < 0
- **Too high**: > 20
- **Invalid types**: Strings, lists, dictionaries, booleans
- **None**: Only invalid for standalone function, allowed in model

## Usage Examples

### SQLAlchemy Model Integration
```python
from models.dog import Dog

# This will automatically validate the age
dog = Dog(name="Buddy", age=5)  # ✅ Valid
dog = Dog(name="Max", age=-1)   # ❌ Raises ValueError
```

### Standalone Validation
```python
from utils.validation import validate_dog_age, is_valid_dog_age

# Exception-based validation
try:
    age = validate_dog_age(5)  # Returns 5
    age = validate_dog_age(-1) # Raises ValueError
except ValueError as e:
    print(f"Invalid age: {e}")

# Boolean-based validation
if is_valid_dog_age(5):   # Returns True
    print("Valid age")
if not is_valid_dog_age(-1):  # Returns False
    print("Invalid age")
```

## Error Messages
- `"Age cannot be negative"` - for negative values
- `"Age cannot be greater than 20 years"` - for values > 20
- `"Age must be a number"` - for non-numeric types
- `"Age cannot be None"` - for None values (standalone function only)

## Testing
All functions have been thoroughly tested with:
- ✅ Valid ages (0, 1, 5, 10, 15, 20, 0.5, 19.9)
- ❌ Invalid negative ages (-1, -5, -10)
- ❌ Invalid high ages (21, 25, 50, 100)
- ❌ Invalid types (strings, lists, dictionaries, booleans)
- ✅ Edge cases (None handling, float values)

Run tests with:
```bash
# Test the model validation
python test_dog_validation.py

# Test the standalone functions
python test_validation.py

# See usage examples
python example_usage.py
```

## Integration
The validation is now integrated into the existing pets-sample project and works with:
- Flask web application
- SQLAlchemy database models
- Existing validation patterns in the codebase
- Current testing framework
