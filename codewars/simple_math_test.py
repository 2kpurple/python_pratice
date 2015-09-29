# reate a function which checks a number for three different properties.

# is the number prime?
# is the number even?
# is the number a multiple of 10?
# Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.

# Examples

# number_property(7)  # ==> [true,  false, false]
# number_property(10) # ==> [false, true,  true]
# The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

# number_property(-7)  # ==> [false, false, false]
# number_property(-10) # ==> [false, true,  true]ki

# coding: utf-8

import math

def number_property(n):
    result = []
    prime = True
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
           if n % i == 0:
                prime = False
                break
    else:
        prime = False
    result.append(prime)
    result.append(n % 2 == 0)
    result.append(n % 10 == 0)
    return result

print number_property(1)
