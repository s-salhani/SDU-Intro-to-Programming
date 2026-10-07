def count_up(n: int) -> None:
    """prints all natural numbers up to n (included), one per line"""

    if n > 0:
        count_up(n - 1)

    print(n)


# the key difference between count_down and count_up is where you put print(n):

# DOWN
#    print(n)
#    count_down(n - 1)

# versus:

# UP
#   count_up(n - 1)
#   print(n)
