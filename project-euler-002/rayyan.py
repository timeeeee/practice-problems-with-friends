'''
METHOD 1
1) Generate fibonacci sequence
2) Save values that are even and do not exceed 4 mil
3) Add saved values
'''

a = 0
b = 1
s = 0
while b <= 4000000:
    if b%2 == 0:
        s = s + b
    a, b = b, a+b
print("Method 1: " + str(s))


