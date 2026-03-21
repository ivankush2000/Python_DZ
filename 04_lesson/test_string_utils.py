import pytest
from string_utils import StringUtils


Utils = StringUtils()


# ------------------capitalize---------------------------
@pytest.mark.parametrize("input, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123", "123")
])
def test_capitalize_positive(input, expected):
    assert Utils.capitalize(input) == expected


def test_capitalize_negative():
    assert Utils.capitalize(" ") == ""


# ------------------trim---------------------------
@pytest.mark.parametrize("input, expected", [
    ("  skypro", "skypro"),
    ("   hello", "hello"),
    ("none", "none"),
    (" 😁😀", "😁😀")
])
def test_trim_positive(input, expected):
    assert Utils.trim(input) == expected


@pytest.mark.parametrize("input, expected", [
    ("", ""),
    ("         ", "")
])
def test_trim_negative(input, expected):
    assert Utils.trim(input) == expected


# -----------------contains------------------
@pytest.mark.parametrize("input1, input2, expected", [
    ("ABC", "A", True),
    ("ABC", "B", True),
    ("ABC", "C", True),
    ("123", "1", True),
    ("ABC", "2", False)
])
def test_contains_positive(input1, input2, expected):
    assert Utils.contains(input1, input2) == expected


@pytest.mark.parametrize("input1, input2, expected", [
    ("ABC", "1", False),
    ("ABC", "a", False),
    ("ABC", "", True),
    (" ", "a", False)
])
def test_contains_negative(input1, input2, expected):
    assert Utils.contains(input1, input2) == expected


# ---------------delete_symbol------------------
@pytest.mark.parametrize("input1, input2, expected", [
    ("1233", "3", "12"),
    ("ABC", "C", "AB"),
    ("ABC.123", ".", "ABC123")
])
def test_delete_symbol_positive(input1, input2, expected):
    assert Utils.delete_symbol(input1, input2) == expected


def test_delete_symbol_negative():
    assert Utils.delete_symbol("   ", " ") == ""