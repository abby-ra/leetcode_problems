def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary
n = 12
print(decimal_to_binary(n))



# output: 1100
# Steps:

# 12 % 2 = 0 → 6
# 6  % 2 = 0 → 3
# 3  % 2 = 1 → 1
# 1  % 2 = 1 → 0


# Binary (reverse order): 1100

# ✅ Output: "1100"
# 🧾 Using Built-in (Python)
# binary = bin(n)[2:]

# ✅ Algorithm (Manual Method)

# If n == 0, return "0"
# While n > 0:
# remainder = n % 2
# append remainder to result
# n = n // 2
# Reverse the result