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
    TrafficLight,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
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

class TestWhiteBoxCalculateOrderTotal(unittest.TestCase):
    """
    White-box tests for calculate_order_total
    """

    # --- Test Cases for 0% Discount (1 <= quantity <= 5) ---

    def test_quantity_minimum_no_discount(self):
        """Checks quantity 1 (lower bound for 0% discount)."""
        items = [{"quantity": 1, "price": 100}]
        self.assertEqual(calculate_order_total(items), 100.0)

    def test_quantity_mid_no_discount(self):
        """Checks quantity 3 (a value within the 0% discount range)."""
        items = [{"quantity": 3, "price": 50}]
        self.assertEqual(calculate_order_total(items), 150.0)

    def test_quantity_maximum_no_discount(self):
        """Checks quantity 5 (upper bound for 0% discount)."""
        items = [{"quantity": 5, "price": 10}]
        self.assertEqual(calculate_order_total(items), 50.0)

    # --- Test Cases for 5% Discount (6 <= quantity <= 10) ---

    def test_quantity_minimum_5_percent_discount(self):
        items = [{"quantity": 6, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 570.0)

    def test_quantity_mid_5_percent_discount(self):
        """Checks quantity 8 (a value within the 5% discount range)."""
        items = [{"quantity": 8, "price": 25}]
        self.assertEqual(calculate_order_total(items), 190.0)

    def test_quantity_maximum_5_percent_discount(self):
        """Checks quantity 10 (upper bound for 5% discount)."""
        items = [{"quantity": 10, "price": 10}]
        self.assertEqual(calculate_order_total(items), 95.0)

    # --- Test Cases for 10% Discount (quantity > 10) ---

    def test_quantity_minimum_10_percent_discount(self):
        """Checks quantity 11 (lower bound for 10% discount)."""
        items = [{"quantity": 11, "price": 10}]
        self.assertAlmostEqual(calculate_order_total(items), 99.0)

    def test_quantity_large_10_percent_discount(self):
        """Checks a large quantity for 10% discount."""
        items = [{"quantity": 20, "price": 50}]
        self.assertAlmostEqual(calculate_order_total(items), 900.0)

    # --- Edge and Combination Test Cases ---

    def test_empty_order(self):
        """Checks an empty list of items."""
        items = []
        self.assertEqual(calculate_order_total(items), 0.0)

    def test_multiple_items_mixed_discounts(self):
        """
        Checks an order with multiple items, each hitting a different discount tier.
        Item 1 (Qty 4): 4 * 10 = 40.00 (0% disc)
        Item 2 (Qty 7): 7 * 20 * 0.95 = 133.00 (5% disc)
        Item 3 (Qty 15): 15 * 5 * 0.9 = 67.50 (10% disc)
        Total Expected: 40.00 + 133.00 + 67.50 = 240.50
        """
        items = [
            {"quantity": 4, "price": 10},
            {"quantity": 7, "price": 20},
            {"quantity": 15, "price": 5},
        ]
        self.assertAlmostEqual(calculate_order_total(items), 240.50)

    def test_zero_quantity_or_price(self):
        """Checks behavior with zero quantity and zero price."""
        items = [
            {"quantity": 0, "price": 10},  
            {"quantity": 5, "price": 0}    
        ]
        self.assertEqual(calculate_order_total(items), 0.0)

class TestWhiteBoxCalculateShippingCost(unittest.TestCase):
    def test_standard_shipping_light_weight_boundary(self):
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_light_weight_inside(self):
        items = [{"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_medium_weight_lower_boundary(self):
        items = [{"weight": 5.1}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_medium_weight_upper_boundary(self):
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_heavy_weight_boundary(self):
        items = [{"weight": 10.1}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_light_weight_boundary(self):
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_medium_weight_lower_boundary(self):
        items = [{"weight": 5.01}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)
        
    def test_express_shipping_medium_weight_upper_boundary(self):
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_heavy_weight_boundary(self):
        items = [{"weight": 10.01}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        items = [{"weight": 1}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "priority")

    def test_empty_order_weight(self):
        items = []
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

class TestWhiteBoxValidateLogin(unittest.TestCase):
    def test_successful_login_minimum_boundary(self):
        self.assertEqual(validate_login("user1", "pass1234"), "Login Successful")

    def test_successful_login_maximum_boundary(self):
        self.assertEqual(validate_login("a" * 20, "p" * 15), "Login Successful")

    def test_successful_login_mid_range(self):
        self.assertEqual(validate_login("miduser", "midpass12"), "Login Successful")

    def test_failed_username_too_short(self):
        self.assertEqual(validate_login("usr", "pass12345678"), "Login Failed")

    def test_failed_username_too_long(self):
        self.assertEqual(validate_login("a" * 21, "pass12345678"), "Login Failed")

    def test_failed_password_too_short(self):
        self.assertEqual(validate_login("validuser", "pass7"), "Login Failed")

    def test_failed_password_too_long(self):
        self.assertEqual(validate_login("validuser", "p" * 16), "Login Failed")

    def test_failed_both_too_short(self):
        self.assertEqual(validate_login("u", "p"), "Login Failed")

    def test_failed_both_too_long(self):
        self.assertEqual(validate_login("a" * 30, "p" * 30), "Login Failed")

    def test_failed_mixed_boundaries(self):
        self.assertEqual(validate_login("abcd", "p" * 15), "Login Failed")
        self.assertEqual(validate_login("a" * 20, "p" * 7), "Login Failed")

class TestWhiteBoxVerifyAge(unittest.TestCase):
    def test_eligible_minimum_boundary(self):
        self.assertEqual(verify_age(18), "Eligible")

    def test_eligible_maximum_boundary(self):
        self.assertEqual(verify_age(65), "Eligible")

    def test_eligible_mid_range(self):
        self.assertEqual(verify_age(30), "Eligible")

    def test_not_eligible_below_minimum_boundary(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_not_eligible_far_below(self):
        self.assertEqual(verify_age(0), "Not Eligible")

    def test_not_eligible_above_maximum_boundary(self):
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_not_eligible_far_above(self):
        self.assertEqual(verify_age(100), "Not Eligible")

class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    def test_category_a_minimum_boundary(self):
        self.assertEqual(categorize_product(10), "Category A")

    def test_category_a_maximum_boundary(self):
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_a_mid_range(self):
        self.assertEqual(categorize_product(30), "Category A")

    def test_category_b_minimum_boundary(self):
        self.assertEqual(categorize_product(51), "Category B")

    def test_category_b_maximum_boundary(self):
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_b_mid_range(self):
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c_minimum_boundary(self):
        self.assertEqual(categorize_product(101), "Category C")

    def test_category_c_maximum_boundary(self):
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_c_mid_range(self):
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d_below_range(self):
        self.assertEqual(categorize_product(9), "Category D")

    def test_category_d_negative_price(self):
        self.assertEqual(categorize_product(-5), "Category D")

    def test_category_d_above_range(self):
        self.assertEqual(categorize_product(201), "Category D")

    def test_category_d_high_price(self):
        self.assertEqual(categorize_product(1000), "Category D")

class TestWhiteBoxValidateEmail(unittest.TestCase):
    def test_valid_email_minimum_boundary(self):
        self.assertEqual(validate_email("a@b.cd"), "Valid Email")

    def test_valid_email_maximum_boundary(self):
        self.assertEqual(validate_email("a" * 24 + "@" + "b" * 23 + ".c"), "Valid Email")

    def test_valid_email_mid_range(self):
        self.assertEqual(validate_email("test.user@domain.com"), "Valid Email")

    def test_invalid_email_too_short_boundary(self):
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_invalid_email_too_long_boundary(self):
        self.assertEqual(validate_email("a" * 25 + "@" + "b" * 24 + ".c"), "Invalid Email")

    def test_invalid_email_missing_at_symbol(self):
        self.assertEqual(validate_email("user.domain.com"), "Invalid Email")

    def test_invalid_email_missing_dot(self):
        self.assertEqual(validate_email("user@domaincom"), "Invalid Email")

    def test_invalid_email_missing_both(self):
        self.assertEqual(validate_email("userdomaincom"), "Invalid Email")

    def test_invalid_email_too_short_but_has_symbols(self):
        self.assertEqual(validate_email("@.a"), "Invalid Email")

    def test_invalid_email_empty_string(self):
        self.assertEqual(validate_email(""), "Invalid Email")
    
class TestWhiteBoxCelsiusToFahrenheit(unittest.TestCase):
    def test_conversion_within_range_zero(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_conversion_within_range_positive(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(10), 50.0)

    def test_conversion_within_range_negative(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0)

    def test_conversion_lower_bound(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_conversion_upper_bound(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_invalid_temperature_below_lower_bound(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_invalid_temperature_above_upper_bound(self):
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_invalid_temperature_far_outside(self):
        self.assertEqual(celsius_to_fahrenheit(500), "Invalid Temperature")

class TestTrafficLight(unittest.TestCase):
    """
    Tests for the TrafficLight class.
    """

    def setUp(self):
        """
        Set up a new TrafficLight instance before each test.
        """
        self.traffic_light = TrafficLight()

    def test_initial_state(self):
        """
        Tests if the initial state is 'Red'.
        """
        self.assertEqual(self.traffic_light.get_current_state(), "Red", "Initial state should be 'Red'")

    def test_state_change_sequence(self):
        """
        Tests the complete sequence of state changes.
        """
        # Initial state is 'Red' from setUp
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green", "State should change from Red to Green")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow", "State should change from Green to Yellow")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red", "State should change from Yellow to Red")

    def test_multiple_cycles(self):
        """
        Tests that the state changes correctly over multiple cycles.
        """
        # Cycle 1
        self.traffic_light.change_state()  # Red -> Green
        self.traffic_light.change_state()  # Green -> Yellow
        self.traffic_light.change_state()  # Yellow -> Red
        self.assertEqual(self.traffic_light.get_current_state(), "Red", "After one full cycle, state should be 'Red'")

        # Cycle 2
        self.traffic_light.change_state()  # Red -> Green
        self.traffic_light.change_state()  # Green -> Yellow
        self.traffic_light.change_state()  # Yellow -> Red
        self.assertEqual(self.traffic_light.get_current_state(), "Red", "After two full cycles, state should be 'Red'")

    def test_get_current_state(self):
        """
        Tests that get_current_state() returns the correct value at all times.
        """
        self.assertEqual(self.traffic_light.get_current_state(), "Red", "get_current_state should return 'Red'")
        
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green", "get_current_state should return 'Green'")
        
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow", "get_current_state should return 'Yellow'")
        
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red", "get_current_state should return 'Red'")





