def count_down_up(n: int) -> None:
    """prints all natural numbers from n to 0 and back to n (included), one per line"""

    print(n)

    if n > 0:
        count_down_up(n - 1)
        print(n)



#print(n)                 # happens going DOWN
#count_down_up(n - 1)     # go deeper
#print(n)                 # happens coming BACK UP
