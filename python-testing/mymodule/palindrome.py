"""Small palindrome script."""

import re


def is_palindrome(name: str) -> bool:
    """Check if input is a palindrome.

    Parameters
    ----------
    name : str
        Name to check

    Returns
    -------
    bool
        True if name was palindrome else False
    """
    if not isinstance(name, str):
        raise TypeError("Only strings are accepted")
    name = re.sub(r"\W+", "", name).replace(" ", "")
    reversed_name = name[::-1]
    if reversed_name.lower() == name.lower():
        return True
    return False
