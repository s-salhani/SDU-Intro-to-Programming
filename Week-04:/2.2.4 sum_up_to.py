def sum_up_to(n: int) -> int:
    """ returns the sum of all natural numbers smaller than or equal to n"""

    if n <= 1:       # base case. <= and not <, because we want it to stop when n reaches 1.
        return 1

    return n + sum_up_to(n - 1) # n - 1 makes the problem smaller each time, and if n <= 1 tells the recursion when to stop.
