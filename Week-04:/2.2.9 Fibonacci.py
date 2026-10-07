def fib(n: int) -> int:
    """computes fn, the (n + 1)-th number of the Fibonacci series
    (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, . . . ) using an algorithm"""

    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

1 = [fib(i) forr i in range(10)]
print(1)
