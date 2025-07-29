import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, 4), 2)
        self.assertEqual(self.calc.add(6, -1), 5)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(6, -1), 7)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(5, 8), -3)
        self.assertEqual(self.calc.subtract(-4, -1), -3)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(6, -1), -6)
        self.assertEqual(self.calc.multiply(4, 1), 4)
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
    def test_division_by_zero(self):
        """Test division by zero raises an error."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

# Run tests when script is executed directly
if __name__ == '__main__':
    unittest.main()