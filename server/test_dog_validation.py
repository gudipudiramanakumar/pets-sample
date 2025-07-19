"""
Test the Dog model validation specifically for age validation.
"""

import sys
import os
import unittest

# Add the server directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# We'll test the validation logic directly since we may not have a full database setup
from models.dog import Dog

class TestDogAgeValidation(unittest.TestCase):
    """Test the age validation in the Dog model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.dog = Dog()
    
    def test_valid_ages(self):
        """Test that valid ages are accepted."""
        valid_ages = [0, 1, 5, 10, 15, 20]
        
        for age in valid_ages:
            with self.subTest(age=age):
                try:
                    result = self.dog.validate_age('age', age)
                    self.assertEqual(result, age)
                except Exception as e:
                    self.fail(f"Valid age {age} should not raise an exception: {e}")
    
    def test_invalid_ages_negative(self):
        """Test that negative ages raise ValueError."""
        invalid_ages = [-1, -5, -10]
        
        for age in invalid_ages:
            with self.subTest(age=age):
                with self.assertRaises(ValueError) as context:
                    self.dog.validate_age('age', age)
                self.assertIn("cannot be negative", str(context.exception))
    
    def test_invalid_ages_too_high(self):
        """Test that ages over 20 raise ValueError."""
        invalid_ages = [21, 25, 50, 100]
        
        for age in invalid_ages:
            with self.subTest(age=age):
                with self.assertRaises(ValueError) as context:
                    self.dog.validate_age('age', age)
                self.assertIn("cannot be greater than 20", str(context.exception))
    
    def test_invalid_age_types(self):
        """Test that non-numeric ages raise ValueError."""
        invalid_types = ["5", "old", [5], {"age": 5}, True]
        
        for age in invalid_types:
            with self.subTest(age=age):
                with self.assertRaises(ValueError) as context:
                    self.dog.validate_age('age', age)
                self.assertIn("must be a number", str(context.exception))
    
    def test_none_age(self):
        """Test that None age is allowed (nullable field)."""
        result = self.dog.validate_age('age', None)
        self.assertIsNone(result)
    
    def test_float_ages(self):
        """Test that float ages are handled correctly."""
        float_ages = [0.5, 1.5, 19.9]
        
        for age in float_ages:
            with self.subTest(age=age):
                try:
                    result = self.dog.validate_age('age', age)
                    self.assertEqual(result, age)
                except Exception as e:
                    self.fail(f"Valid float age {age} should not raise an exception: {e}")

def run_tests():
    """Run the dog age validation tests."""
    print("Running Dog model age validation tests...\n")
    
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDogAgeValidation)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, failure in result.failures:
            print(f"  {test}: {failure}")
    
    if result.errors:
        print("\nErrors:")
        for test, error in result.errors:
            print(f"  {test}: {error}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
