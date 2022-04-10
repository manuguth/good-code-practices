def is_palindrome(name: str) -> bool:
    reversed_name = name[::-1]
    if reversed_name == name:
        return True
    else:
        return False

