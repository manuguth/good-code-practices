"""Small palindrome script."""

import re


def is_palindrome(name: str) -> bool:
    """Check if an expression is a palindrome.

    Parameters
    ----------
    name: expression to be checked

    Returns
    -------
    is_panlindrom: boolean expression stating if name is palindrome
    """
    if type(name) is not str:
        raise TypeError("Only strings are accepted")
    name = re.sub(r"\W+", "", name).replace(" ", "")
    reversed_name = name[::-1]
    if reversed_name.lower() == name.lower():
        return True
    return False
