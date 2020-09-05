from itertools import takewhile

from nose.tools import *


def fibonacci(max=None):
    a = 0
    b = 1
    while max is None or b < max:
        yield b
        a, b = b, a + b


def test_fibonacci_generator():
    generator = fibonacci()
    fib = []
    for _ in range(10):
        fib.append(next(generator))

    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert_list_equal(fib, expected)


def is_even(n):
    return (n % 2 == 0)


if __name__ == "__main__":
    # gross:
    # sum(filter(is_even, takewhile(lambda n: n < 4000000, fibonacci())))
    less_than_4m = (lambda n: n < 4000000)
    fibs_under_4m = takewhile(less_than_4m, fibonacci())
    print(sum(filter(is_even, fibs_under_4m)))
