# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    VendingMachine,
    calculate_total_discount,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


class TestWhiteBoxCheckNumberStatus(unittest.TestCase):
    """
    White-box tests for check_number_status.
    """

    def test_check_number_status_positive(self):
        """Checks when the number is positive."""
        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """Checks when the number is negative."""
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        """Checks when the number is zero."""
        self.assertEqual(check_number_status(0), "Zero")


class TestWhiteBoxValidatePassword(unittest.TestCase):
    """
    White-box tests for validate_password.
    """

    def test_validate_password_too_short(self):
        """Checks when the password length is less than 8."""
        self.assertFalse(validate_password("Ab2?"))

    def test_validate_password_missing_uppercase(self):
        """Checks when the password has no uppercase letter."""
        self.assertFalse(validate_password("abcdefgh"))

    def test_validate_password_missing_lowercase(self):
        """Checks when the password has no lowercase letter."""
        self.assertFalse(validate_password("ABCDEFGH"))

    def test_validate_password_missing_digit_and_special(self):
        """Checks when the password has no digit and no special character."""
        self.assertFalse(validate_password("Abcdefgh"))

    def test_validate_password_missing_special(self):
        """Checks when the password has no special character."""
        self.assertFalse(validate_password("Abcdefg2"))

    def test_validate_password_missing_digit(self):
        """Checks when the password has no digit."""
        self.assertFalse(validate_password("Abcdefg?"))

    def test_validate_password_valid(self):
        """Checks when the password meets all requirements."""
        self.assertTrue(validate_password("Abcd123!"))


class TestWhiteBoxCalculateTotalDiscount(unittest.TestCase):
    """
    White-box tests for calculate_total_discount.
    """

    def test_calculate_total_discount_below_100(self):
        """Checks when total amount is below 100."""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_equal_100(self):
        """Checks when total amount is exactly 100."""
        self.assertEqual(calculate_total_discount(100), 10.0)

    def test_calculate_total_discount_between_100_and_500(self):
        """Checks when total amount is between 100 and 500."""
        self.assertEqual(calculate_total_discount(200), 20.0)

    def test_calculate_total_discount_equal_500(self):
        """Checks when total amount is exactly 500."""
        self.assertEqual(calculate_total_discount(500), 50.0)

    def test_calculate_total_discount_above_500(self):
        """Checks when total amount is greater than 500."""
        self.assertEqual(calculate_total_discount(700), 140.0)
