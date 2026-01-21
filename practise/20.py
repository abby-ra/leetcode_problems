def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    return total == num

num = int(input("Enter a number: "))
print(is_armstrong(num))

# Program for Armstrong Numbers

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

# Examples

# Input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input: n = 9474
# Output: true
# Explanation: 94 + 44 + 74 + 44 = 6561 + 256 + 2401 + 256 = 9474

# Input: n = 123
# Output: false
# Explanation: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36