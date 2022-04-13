"""Unit tests of palindrome."""
import pytest
from mymodule import is_palindrome


@pytest.mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("ABBA", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    """Check the examples given in pytest.mark.parametrize."""
    assert is_palindrome(maybe_palindrome) == expected_result


def test_fails_no_string():
    """Checks if error is raised if no string is provided."""
    with pytest.raises(TypeError) as e_info:
        is_palindrome(22)
    assert str(e_info.value) == "Only strings are accepted"
