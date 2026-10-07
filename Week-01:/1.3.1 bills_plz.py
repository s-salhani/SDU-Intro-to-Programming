def round_up(x : float) -> int:
    """ Rounds up a floating number."""
    # integer division by 1 rounds down: 1.1 // 1 is 1.0, -1.1 // 1 is -2.0
    # so we negate, divide, and negate again to round up before truncating
    # the result to an integer.
    return int(-(-x // 1))

def bill_quota(bill : float, tip : float, people: int) -> int:
    """
    Returns the amount each person needs to contribute to cover a bill and
    the corresponding tipping percentage (0.2 is a 20% tip).
    
    precondiiton: people > 0

    >>> bill_quota(100.0, 0.2 4)
    30
    >>> bill_quota(100.0, 0.2 2)
    60
    >>> bill_quota(100.0, 0.2 7)
    18
    """"
    total : float = bill + bill * tip
    quota : int = round_up(total / people)
    return quota



# or using if-statements

def bill_quota(bill : float, tip : float, people: int) -> int:
    """
    Returns the amount each person needs to contribute to cover a bill and
    the corresponding tipping percentage (0.2 is a 20% tip).
    """
    if (people < 1):
        raise ValueError ("people cannot be less than 1")
    if (bill <= 0):
        raise ValueError ("Bill cannot be less than 0")
    if (tip > 1, tip < 0):
        raise ValueError ("tip cannot be between 1 and 1")

    total : float = bill + bill * tip
    quota : int = round_up(total / people)
    return quota
