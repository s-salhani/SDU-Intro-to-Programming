def gcd(m: int, n: int) -> int:
    """returns the greatest common divisor of m and n using Euclides’ algorithm"""

    if m == n:
        return m

    if m < n:
        return gcd(m, n - m)

    if m > n:
        return gcd(m - n,m)
