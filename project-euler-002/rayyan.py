from math import factorial as fact
'''
METHOD 1
1) Generate fibonacci sequence
2) Save values that are even and do not exceed 4 mil
3) Add saved values
'''

a, b, s = 0, 1, 0  # First fib value, second fib value, current sum
while b <= 4000000:  # Boundary for sum
    if b % 2 == 0:  # Determines next fib value is even. If so, add it to sum
        s = s + b
    a, b = b, a+b
print("Method 1: " + str(s))  # Prints final sum

'''
METHOD 2: Same as method 1, but with functions
'''

def fib(n):
    pass

'''
while True:
    final_result = 0
    for n in range(0, 4000001):
        print fib(n)
        if fib(n) % 2 == 0:
            final_result = final_result + fib(n)
    print("Method 2: " + str(final_result))
    break
'''
