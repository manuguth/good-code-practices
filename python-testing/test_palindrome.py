from mymodule import is_palindrome
import pytest


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
    assert is_palindrome(maybe_palindrome) == expected_result


def test_fails_no_string():
    with pytest.raises(TypeError) as e_info:
        is_palindrome(22)
    assert str(e_info.value) == "Only strings are accepted"
