# Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits(n):
    count = 0
    while n >= 1:
        n = n & (n - 1)
        count += 1
    return count

print countBits(1234)
