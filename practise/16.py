# Pair Cube Count

# Examples: 
# Input: n = 9
# Output: 2
# Explanation: 1^3 + 2^3 = 9 and 2^3 + 1^3 = 9

# Input: n = 28
# Output: 2
# Explanation: 1^3 + 3^3 = 28 and 3^3 + 1^3 = 28



# PROGRAM:


def count_pairs(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(n + 1):
            if a**3 + b**3 == n:
                count += 1
    return count

n = 9
print(count_pairs(n))