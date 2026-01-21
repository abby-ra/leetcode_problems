def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def add_fractions(a, b):
    num1, den1 = a
    num2, den2 = b

    numerator = num1 * den2 + num2 * den1
    denominator = den1 * den2

    g = gcd(numerator, denominator)

    return [numerator // g, denominator // g]



# a = [1, 2]
# b = [3, 2]

# Numerator   = (1×2) + (3×2) = 8
# Denominator = 2×2 = 4
# Simplified  = 8/4 = 2/1

# Output: [2, 1]
