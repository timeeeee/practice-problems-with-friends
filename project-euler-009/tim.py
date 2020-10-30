"""
The brute force way: check every valid (a, b, max_sum - a - b) triple to see if
it's a pythagorean triple. Complexity is O(n**2).

For me this takes ~14 seconds to find find a solution for n = 10000, or that
there's no solution for n = 9999.

The faster solution comes from:
- https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
- https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs

Where m and n are positive coprime integers where m > n and one is even, all
primitive pythagorean triples can be generated using the equations:
a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

The function primitive_triple_generator generates pairs (m, n) and then
converts them into pythagorean triples, and the function triple_with_sum checks
each primitive to see if there's a value k so that k * (a + b + c) == max_sum.

Calculating the complexity of this is scary but it should be proportional to
the number of primitive triples with sums < max_sum, and that looks *super*
linear!

max_sum, number of primitive triples:
10**2, 7
10**3, 70
10**4, 703
10**5, 7026
10**6, 70229
10**7, 702309
10**8, 7023027

so it looks like this is O(n)! triple_with_sum(10**8 - 1) took ~51 seconds for
me.
"""

from math import sqrt, gcd

from nose.tools import *


def brute_force_triple_with_sum(n):
    """
    Find the first pythagorean triple (a, b, c) such that a + b + c == n, or
    return None if none exists.

    The lowest pythagorean triple is (3, 4, 5) so start guessing a at 3.

    b > a so start guessing b at a + 1

    Once I've guessed a and b, set c = n - a - b and check if
    a**2 + b**2 == c**2. If a**2 + b**2 > c**2, b is too big.

    if n - a - (a + 1) == a + 1 then b == c and a is too high. So
    n - a_max - (a_max + 1) = a_max + 2
    n = 3 * a_max + 3
    a_max = n / 3 - 1

    Complexity
    ==========

    a ranges from a constant to n / 3
    b ranges from a + a constant to wherever a**2 + b**2 == c**2
    a**2 + b**2 = (n - a - b)**2 = n**2 + a**2 + b**2 - 2na - 2nb + 2ab
        => n**2 - 2na - 2nb + 2ab = 0
        => n**2 - 2na = 2nb - 2ab = b * 2 * (n - a)
        => b = (n**2 - 2na) / (2n - 2a)
    lim (n -> inf) b = n

    SO for a in range(n) for b in range(n) check for a solution
        => O(n**2)
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


def coprimes_to_pythagorean_triple(m, n):
    """
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2

    assuming that:
        m, n are positive integers
        m > n
        m and n are coprime
        m and n are not both odd
    """
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2

    if a > b:
        a, b = b, a

    return (a, b, c)


def primitive_triple_generator(maximum):
    # yield from primitive_triple_generator_recursive((2, 1), maximum)
    yield from primitive_triple_generator_iterative(maximum)


def primitive_triple_generator_recursive(node, maximum):
    m, n = node
    triple = coprimes_to_pythagorean_triple(m, n)
    if sum(triple) > maximum:
        return

    yield triple

    # now do the branches
    yield from primitive_triple_generator_recursive((2 * m - n, m), maximum)
    yield from primitive_triple_generator_recursive((2 * m + n, m), maximum)
    yield from primitive_triple_generator_recursive((m + 2 * n, n), maximum)


def primitive_triple_generator_iterative(maximum):
    """
    from https://en.wikipedia.org/wiki/Coprime_integers
    All pairs of positive coprime numbers (m, n) (with m > n) be arranged in
    two disjoint complete ternary trees, one tree starting from (2, 1) (for
    even-odd and odd-even pairs), and the other tree starting from (3, 1) (for
    odd-odd pairs).

    The children of each vertex (m, n) are generated as follows:
    branch 1: 2 * m - n, m
    branch 2: 2 * m + n, m
    branch 3: m + 2n, n

    Some algebra leads me to think that:
    - a + b + c for the corresponding pythagorean triple of a pair (m, n) is
      always greater than a + b + c for its parent

    SO to do a traversal of this tree, make a stack of pairs (m, n) starting
    with (2, 1). It doesn't matter what order the traversal is in, but
    list.pop() is O(1) and list.pop(0) is O(n)! so do it depth-first. Once a
    pair results in a triple with a sum that's too high, we know all of its
    children will also be too high so we can stop exploring that branch.
    """
    stack = [(2, 1)]
    while len(stack) > 0:
        m, n = stack.pop()
        triple = coprimes_to_pythagorean_triple(m, n)

        # if this sum is too high we don't have to visit its branches
        if sum(triple) > maximum:
            continue

        yield triple

        stack.append((2 * m - n, m))  # branch 1
        stack.append((2 * m + n, m))  # branch 2
        stack.append((m + 2 * n, n))  # branch 3


def test_primitive_triple_generator_recursive():
    expected = set([
        (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
        (12, 35, 37), (9, 40, 41), (28, 45, 53), (11, 60, 61), (16, 63, 65),
        (33, 56, 65), (48, 55, 73), (13, 84, 85), (36, 77, 85), (39, 80, 89),
        (20, 99, 101), (65, 72, 97), (15, 112, 113), (60, 91, 109),
        (44, 117, 125), (17, 144, 145), (24, 143, 145), (88, 105, 137),
        (51, 140, 149), (85, 132, 157), (19, 180, 181), (52, 165, 173),
        (119, 120, 169), (57, 176, 185), (28, 195, 197), (104, 153, 185),
        (95, 168, 193), (21, 220, 221), (84, 187, 205), (133, 156, 205),
        (60, 221, 229), (140, 171, 221), (32, 255, 257), (105, 208, 233),
        (23, 264, 265), (120, 209, 241), (69, 260, 269), (96, 247, 265),
        (115, 252, 277), (68, 285, 293), (25, 312, 313), (160, 231, 281),
        (36, 323, 325), (161, 240, 289), (75, 308, 317), (136, 273, 305),
        (207, 224, 305), (27, 364, 365), (204, 253, 325), (76, 357, 365),
        (175, 288, 337), (180, 299, 349), (40, 399, 401), (225, 272, 353),
        (135, 352, 377), (29, 420, 421), (152, 345, 377), (252, 275, 373),
        (189, 340, 389), (120, 391, 409), (87, 416, 425), (228, 325, 397),
        (84, 437, 445), (145, 408, 433), (31, 480, 481)
    ])

    assert_set_equal(
        set(primitive_triple_generator_recursive((2, 1), 1000)),
        expected
    )


def test_primitive_triple_generator_iterative():
    expected = set([
        (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
        (12, 35, 37), (9, 40, 41), (28, 45, 53), (11, 60, 61), (16, 63, 65),
        (33, 56, 65), (48, 55, 73), (13, 84, 85), (36, 77, 85), (39, 80, 89),
        (20, 99, 101), (65, 72, 97), (15, 112, 113), (60, 91, 109),
        (44, 117, 125), (17, 144, 145), (24, 143, 145), (88, 105, 137),
        (51, 140, 149), (85, 132, 157), (19, 180, 181), (52, 165, 173),
        (119, 120, 169), (57, 176, 185), (28, 195, 197), (104, 153, 185),
        (95, 168, 193), (21, 220, 221), (84, 187, 205), (133, 156, 205),
        (60, 221, 229), (140, 171, 221), (32, 255, 257), (105, 208, 233),
        (23, 264, 265), (120, 209, 241), (69, 260, 269), (96, 247, 265),
        (115, 252, 277), (68, 285, 293), (25, 312, 313), (160, 231, 281),
        (36, 323, 325), (161, 240, 289), (75, 308, 317), (136, 273, 305),
        (207, 224, 305), (27, 364, 365), (204, 253, 325), (76, 357, 365),
        (175, 288, 337), (180, 299, 349), (40, 399, 401), (225, 272, 353),
        (135, 352, 377), (29, 420, 421), (152, 345, 377), (252, 275, 373),
        (189, 340, 389), (120, 391, 409), (87, 416, 425), (228, 325, 397),
        (84, 437, 445), (145, 408, 433), (31, 480, 481)
    ])

    assert_set_equal(
        set(primitive_triple_generator_iterative(1000)),
        expected
    )


def triple_with_sum(n):
    for a, b, c in primitive_triple_generator(n):
        # is there a k so that k (a + b + c) == n?
        k, remainder = divmod(n, a + b + c)
        if remainder == 0:
            return k * a, k * b, k * c

    return None


SOLUTIONS = [brute_force_triple_with_sum, triple_with_sum]


def test_pythagorean_triple_12():
    for func in SOLUTIONS:
        yield (assert_tuple_equal, func(12), (3, 4, 5))


def test_pythagorean_triple_12():
    for func in SOLUTIONS:
        yield (assert_tuple_equal, func(24), (6, 8, 10))


def test_pythagorean_triple_30():
    for func in SOLUTIONS:
        yield (assert_tuple_equal, func(30), (5, 12, 13))


def test_pythagorean_triple_40():
    for func in SOLUTIONS:
        yield (assert_tuple_equal, func(40), (8, 15, 17))


def test_pythagorean_triple_none():
    sums = set([12, 24, 30, 36, 40, 48])
    for n in range(1, 56):
        if n not in sums:
            for func in SOLUTIONS:
                yield assert_is_none, func(n)


if __name__ == "__main__":
    a, b, c = triple_with_sum(1000)
    print(a * b * c)
