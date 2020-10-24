# Write a program that statisfies:
# a < b < c, a2 + b2 = c2 and a + b + c = 1000. Output a * b * c

# Method 1: Brute force. Slow.

import sys

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a < b and b < c and a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a * b * c)
                sys.exit()
