"""
Some tricks I am trying:

Rather than finding all factors, calculate # of factors from prime factors
cache prime factorizations (seems to bump time up by ~20%)
instead of factoring a triangle number n * (n + 1) / 2:
    combine prime factors of n and n + 1, and remove a 2
"""


from collections import Counter, defaultdict
from nose.tools import *


CACHE = dict()


def prime_factors(n):
    """
    return a tuple of the prime factors of n
    """
    factors = []
    # try 2 first
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    if n > 1:
        factors.extend(prime_factors_of_odd_number(n))

    return factors


def prime_factors_of_odd_number(n):
    try:
        return CACHE[n]
    except KeyError:
        # if the answer is not already in the cache, calculate it:
        factor = 3
        while factor * factor <= n:
            if n % factor == 0:
                factors = [factor]
                # RECURSE to get the rest of the factors
                factors.extend(prime_factors_of_odd_number(n // factor))
                break
            factor += 2
        else:
            # if we didn't find a factor- this number is prime!
            factors = [n]

        CACHE[n] = factors
        return factors


def test_prime_factors():
    data = [
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (5, [5]),
        (6, [2, 3]),
        (7, [7]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (10, [2, 5]),
        (11, [11]),
        (60, [2, 2, 3, 5]),
        (61, [61]),
    ]

    for n, expected in data:
        assert_list_equal(expected, prime_factors(n))


def prime_factor_count_of_nth_triangle(n):
    # triangle number = n * (n + 1) / 2
    count = Counter(prime_factors(n))
    count.update(prime_factors(n + 1))
    count.subtract([2])
    return count


def test_prime_factor_count_of_nth_triangle():
    # check triangle numbers 2-11
    for n in range(2, 12):
        triangle = n * (n + 1) // 2
        expected = Counter(prime_factors(triangle))
        if 2 not in expected:
            expected[2] = 0

        assert_dict_equal(
            prime_factor_count_of_nth_triangle(n),
            expected)


def product(sequence):
    x = 1
    for n in sequence:
        x *= n
    return x


def num_factors_from_prime_factors(prime_counts):
    """
    If a numbers prime factors are 2**2 * 3, a factor can be made with either
    zero, one, or two 2's, and zero or one 3's:
    1, 2, 2 * 2, 3, 2 * 3, 2 * 2 * 3

    So for the number 2**a * 3**b * 5 ** c * 7**d... the number of factors is
    (a + 1) * (b + 1) * (c + 1) * (d + 1)...
    """
    return product(n + 1 for n in prime_counts.values())


def test_num_factors_from_prime_factors():
    data = [
        (Counter([3]), 2),
        (Counter([2, 2]), 3),
        (Counter([2, 3]), 4),
        (Counter([2, 2, 2]), 4),
        (Counter([3, 3]), 3),
        (Counter([2, 2, 3, 3]), 9),
        (Counter([2, 2, 3, 5]), 12),
        (Counter([2, 3, 5, 7]), 16),
    ]

    for counter, num_factors in data:
        assert_equal(num_factors_from_prime_factors(counter), num_factors)


if __name__ == "__main__":
    n = 2
    while True:
        triangle = n * (n + 1) // 2
        p_factors = prime_factor_count_of_nth_triangle(n)
        num_factors = num_factors_from_prime_factors(p_factors)
        if False:
            print("triangle({}): {} = {} and has {} factors".format(
                n, triangle, p_factors, num_factors))

        if num_factors > 500:
            break

        n += 1

    print(triangle)
