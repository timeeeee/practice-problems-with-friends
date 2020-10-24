from nose.tools import *


def pythagorean_triple_with_sum(n):
    """
    Find the first pythagorean triple (a, b, c) such that a + b + c == n, or
    return None if none exists.

    The lowest pythagorean triple is (3, 4, 5) so start guessing a at 3.

    So that I only guess a pair (a, b) once, start guessing b at (a + 1).

    Once I've guessed a and b, set c = n - a - b and check if
    a**2 + b**2 == c**2. If a**2 + b**2 > c**2, b is too big.

    if n - a - (a + 1) == a + 1 then b == c and a is too high. So
    n - a_max - (a_max + 1) = a_max + 2
    n = 3 * a_max + 3
    a_max = n / 3 - 1
    """
    for a in range(3, n // 3):
        b = a + 1
        while True:
            c = n - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)
            elif a**2 + b**2 > c**2:
                break

            b += 1


def test_pythagorean_triple_12():
    assert_tuple_equal(pythagorean_triple_with_sum(12), (3, 4, 5))


def test_pythagorean_triple_12():
    assert_tuple_equal(pythagorean_triple_with_sum(24), (6, 8, 10))


def test_pythagorean_triple_30():
    assert_tuple_equal(pythagorean_triple_with_sum(30), (5, 12, 13))


def test_pythagorean_triple_40():
    assert_tuple_equal(pythagorean_triple_with_sum(40), (8, 15, 17))


def test_pythagorean_triple_none():
    sums = set([12, 24, 30, 36, 40, 48])
    for n in range(1, 56):
        if n not in sums:
            assert_is_none(pythagorean_triple_with_sum(n))


if __name__ == "__main__":
    a, b, c = pythagorean_triple_with_sum(1000)
    print(a * b * c)
