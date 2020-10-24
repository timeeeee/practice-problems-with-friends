'''
METHOD 1
1) Read in number into integer variable)
2) Loop through length-13
3) For each loop, multiply the first 13 digits
4) Compare to last product. If higher, save that one.
5) Do this till you've finished the entire number
6) Print out the highest product
'''

# Read in number
n = open('number.txt', 'r')
number = n.read()
n.close()

# Loop through number
highest_product = 0
for i in range(len(number)-13):
    temp_product = 1
    for x in range(13):
        temp_product = temp_product * int(number[x+i])
    if temp_product > highest_product:
        highest_product = temp_product
print("Method 1: " + str(highest_product))
