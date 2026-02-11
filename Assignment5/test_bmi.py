import unittest
from bmi import BMI

class TestBMI(unittest.TestCase):
    def test_calculation(self):
        person = BMI(70, 1.75)
        self.assertEqual(person.calculate_bmi(), 22.86)

    def test_underweight(self):
        person = BMI(45, 1.75)
        self.assertEqual(person.get_category(), "Underweight")

    def test_zero_height(self):
        # Testing edge case to avoid division by zero
        person = BMI(70, 0)
        self.assertEqual(person.calculate_bmi(), 0)

if __name__ == "__main__":
    unittest.main()