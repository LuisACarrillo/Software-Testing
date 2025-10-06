# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import MagicMock, mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case for fetch_data_from_api.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}
        mock_get.return_value.status_code = 200

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


# ---
class TestFileOperations(unittest.TestCase):
    """
    File operations unittest class.
    """

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="Contenido del archivo de prueba",
    )
    def test_read_data_from_file_success(self, mock_file):
        """
        Success case for read_data_from_file.
        """
        filename = "test_file.txt"
        expected_data = "Contenido del archivo de prueba"

        # Call the function under test
        result = read_data_from_file(filename)

        # Assert that the function returns the expected result
        self.assertEqual(result, expected_data)

        # Assert that the file was opened with the correct arguments
        mock_file.assert_called_once_with(filename, encoding="utf-8")


# ---
class TestCommandExecutor(unittest.TestCase):
    """
    Command executor unittest class.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case for execute_command.
        """
        command = ["ls", "-l"]
        expected_output = "stdout de prueba"

        # Set up the mock subprocess result
        mock_result = MagicMock()
        mock_result.stdout = expected_output
        mock_run.return_value = mock_result

        # Call the function under test
        result = execute_command(command)

        # Assert that the function returns the expected result
        self.assertEqual(result, expected_output)

        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )


# ---
class TestTimeBasedActions(unittest.TestCase):
    """
    Time-based actions unittest class.
    """

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Case where current time is less than 10 (Action A).
        """
        # Mock time.time() to return a value less than 10
        mock_time.return_value = 5.0

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert the expected action is returned
        self.assertEqual(result, "Action A")

        # Assert that time.time() was called
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Case where current time is 10 or greater (Action B).
        """
        # Mock time.time() to return a value greater than or equal to 10
        mock_time.return_value = 15.0

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert the expected action is returned
        self.assertEqual(result, "Action B")

        # Assert that time.time() was called
        mock_time.assert_called_once()
