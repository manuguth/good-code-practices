"""Small palindrome script."""


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
    reversed_name = name[::-1]
    if reversed_name == name:
        return True

    return False
