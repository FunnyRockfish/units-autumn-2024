import unittest
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.addition(3, 2), 5)

    def test_addition_positive_numbers_inf(self):
        self.assertEqual(self.calc.addition(3, math.inf), math.inf)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.addition(-1, 1), 0)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.addition(-1, -1), -2)

    def test_addition_with_inf_and_negative(self):
        self.assertEqual(self.calc.addition(-math.inf, 1), -math.inf)

    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiplication(3, 2), 6)

    def test_multiplication_with_negative_number(self):
        self.assertEqual(self.calc.multiplication(-1, 1), -1)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiplication(0, 100), 0)

    def test_multiplication_with_inf_1(self):
        self.assertEqual(self.calc.multiplication(2, math.inf), math.inf)

    def test_multiplication_with_inf_2(self):
        self.assertEqual(self.calc.multiplication(-1, math.inf), -math.inf)

    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtraction(3, 2), 1)

    def test_subtraction_resulting_in_negative(self):
        self.assertEqual(self.calc.subtraction(2, 3), -1)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtraction(-1, -1), 0)

    def test_subtraction_with_inf_1(self):
        self.assertEqual(self.calc.subtraction(math.inf, 1), math.inf)

    def test_subtraction_with_inf_2(self):
        self.assertEqual(self.calc.subtraction(-math.inf, 1), -math.inf)

    def test_division_normal_case(self):
        self.assertEqual(self.calc.division(6, 3), 2)

    def test_division_period(self):
        self.assertAlmostEqual(self.calc.division(1, 3), 1/3, places=6)

    def test_division_fractional_result(self):
        self.assertEqual(self.calc.division(5, 2), 2.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.division(5, 0))  # Негативный кейс

    def test_division_with_inf_1(self):
        self.assertEqual(self.calc.division(5, math.inf), 0)

    def test_division_with_inf_2(self):
        self.assertEqual(self.calc.division(math.inf, 2), math.inf)

    def test_absolute_negative_number(self):
        self.assertEqual(self.calc.absolute(-5), 5)

    def test_absolute_positive_number(self):
        self.assertEqual(self.calc.absolute(5), 5)

    def test_absolute_inf(self):
        self.assertEqual(self.calc.absolute(math.inf), math.inf)

    def test_degree_positive_exponent(self):
        self.assertEqual(self.calc.degree(2, 3), 8)

    def test_negative_degree(self):
        self.assertEqual(self.calc.degree(4, -1), 0.25)

    def test_degree_zero_exponent(self):
        self.assertEqual(self.calc.degree(5, 0), 1)

    def test_degree_with_inf(self):
        self.assertEqual(self.calc.degree(math.inf, 2), math.inf)

    def test_ln_positive_number(self):
        self.assertAlmostEqual(self.calc.ln(math.e), 1, places=7)

    def test_ln_negative_number(self):
        with self.assertRaises(ValueError):
            self.calc.ln(-1)  # негативный кейс

    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            self.calc.ln(0)

    def test_ln_inf(self):
        self.assertEqual(self.calc.ln(math.inf), math.inf)

    def test_ln_fractional_number(self):
        self.assertAlmostEqual(self.calc.ln(5/3), 0.5108256, places=7)

    def test_log_valid_base(self):
        self.assertAlmostEqual(self.calc.log(8, 2), 3, places=7)

    def test_log_negative_number(self):
        with self.assertRaises(ValueError):
            self.calc.log(-1, 2)  # негативный кейс

    def test_log_inf(self):
        self.assertEqual(self.calc.log(math.inf, 2), math.inf)

    def test_sqrt_positive_number(self):
        self.assertAlmostEqual(self.calc.sqrt(4), 2, places=7)

    def test_sqrt_another_positive_number(self):
        self.assertAlmostEqual(self.calc.sqrt(9), 3, places=7)

    def test_sqrt_inf(self):
        self.assertEqual(self.calc.sqrt(math.inf), math.inf)

    def test_nth_root_valid_case(self):
        self.assertAlmostEqual(self.calc.nth_root(8, 3), 2, places=7)

    def test_root_null(self):
        self.assertAlmostEqual(self.calc.nth_root(0, 2), 0)

    def test_nth_root_another_valid_case(self):
        self.assertAlmostEqual(self.calc.nth_root(27, 3), 3, places=7)

    def test_nth_root_with_inf(self):
        self.assertEqual(self.calc.nth_root(math.inf, 2), math.inf)

if __name__ == "__main__":
    unittest.main()
