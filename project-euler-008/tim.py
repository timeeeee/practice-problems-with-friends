"""
The straightforward way to do this has complexity O(m * n) where m is the
number of digits in the sequence, and n is the number of consecutive numbers to
take the product of. simple_max_product(digits, n) implements this.

By using a queue to store a sliding window of digits, popping off the oldest
value and adding the new one each time the window moves, the space complexity
is limited to O(n).

Aaaand by keeping a running product (of all non-zero digits), multiplying by
a number as it enters the window and dividing by it when it exits, the time
complexity is O(m). max_product(digits, n) implements this.
"""


from nose.tools import *


def prod(seq):
    result = 1
    for n in seq:
        result *= n

    return result


def test_prod_empty_list():
    assert_equal(prod([]), 1)


def test_prod_range():
    assert_equal(prod(range(1, 10)), 362, 880)


def test_prod_range_with_zero():
    assert_equal(prod(range(10)), 0)


def file_char_generator(flo):
    while True:
        try:
            digit = int(flo.read(1))
            yield digit
        except ValueError:
            break


def test_file_char_generator():
    with open("number.txt") as f:
        numbers_from_file = [int(char) for char in f.read().strip()]

    with open("number.txt") as f:
        numbers_from_generator = list(file_digit_generator(f))

    assert_list_equal(numbers_from_file, numbers_from_generator)


def simple_max_product(digits, n):
    """
    Take a LIST of digits.

    Time complexity: O(len(digits) * n)
    Space complexity: O(len(digits))
    """
    max_product = 0
    for start in range(len(digits) - n + 1):
        end = start + n
        product = prod(digits[start:end])
        if product > max_product:
            max_product = product

    return max_product


def max_product(digits, n):
    """
    Takes an iterator of digits. Keep a running product of the digits in the
    window, skipping (but counting) zeros.

    Time complexity: O(len(digits))
    Space complexity: O(n)
    """
    # Get the first window
    window = []
    product = 1  # product of everything in the window that's not zero
    zero_count = 0
    for _ in range(n):
        digit = next(digits)
        window.append(digit)
        if digit == 0:
            zero_count += 1
        else:
            product *= digit

    if zero_count == 0:
        max_product = product
    else:
        max_product = 0

    # now for the rest of the digits...
    for digit in digits:
        old_digit = window.pop(0)
        window.append(digit)

        # divide by the oldest digit, or decrement zero_count
        if old_digit == 0:
            zero_count -= 1
        else:
            product //= old_digit

        # multiply by the new digit, or increment zero_count
        if digit == 0:
            zero_count += 1
        else:
            product *= digit

        # if there are no zeros, "product" is the *real* current product
        if zero_count == 0 and product > max_product:
            max_product = product

    return max_product


if __name__ == "__main__":
    with open("number.txt") as f:
        print(max_product(file_char_generator(f), 13))
