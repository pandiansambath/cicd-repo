import pytest
from unittest.mock import patch
from calc import add, subtract, multiply, divide, calculator

def test_add():
    assert add(5, 3) == 8
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)

@patch("builtins.input", side_effect=["1", "10", "5", "5"])  # Add option
@patch("builtins.print")
def test_calculator_add(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Result: 15.0")

@patch("builtins.input", side_effect=["2", "15", "5", "5"])  # Subtract option
@patch("builtins.print")
def test_calculator_subtract(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Result: 10.0")

@patch("builtins.input", side_effect=["3", "3", "4", "5"])  # Multiply option
@patch("builtins.print")
def test_calculator_multiply(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Result: 12.0")

@patch("builtins.input", side_effect=["4", "20", "4", "5"])  # Divide option
@patch("builtins.print")
def test_calculator_divide(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Result: 5.0")

@patch("builtins.input", side_effect=["4", "10", "0", "5"])  # Divide by zero
@patch("builtins.print")
def test_calculator_divide_by_zero(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Error: Cannot divide by zero!. Please enter valid inputs.")

@patch("builtins.input", side_effect=["5"])  # Exit option
@patch("builtins.print")
def test_calculator_exit(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Exiting the calculator. Goodbye!")
