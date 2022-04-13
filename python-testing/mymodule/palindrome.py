"""Small palindrome script."""


def is_palindrome(name: str) -> bool:
    """Check if an expression is a palindrome.

    Parameters
    ----------
    name: expression to be checked

    Returns
    -------
    is_panlindrom: boolean expression stating if name is palindrome

    """
    reversed_name = name[::-1]
    if reversed_name == name:
        return True

    return False
