def count_down(n: int) -> None:
    """prints all natural numbers from n down to 0 (included), one per line"""
    print(n)

    if n > 0:
        count_down(n - 1)
