def sign(n : float) -> int:
    """ returns the sign of the number n"""
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
