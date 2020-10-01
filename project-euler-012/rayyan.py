'''

1) Pick a natural number
2) Find number of divisors
3) If number > 500 --> Sum the divisors

'''
import sys, math

x = 1
while True:
    s = 0
    t = int((x*(x+1))/2)
    for y in range(1,int(math.sqrt(t+1))):
        if t%y == 0:
            if t/y == y:
                s = s+1
            else:
                s = s+2
    if s > 500:
        print(t)
        sys.exit()
    x = x+1
