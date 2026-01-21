def is_power(x, y):
    if y == 1:
        return True

    while y > 1:
        if y % x != 0:
            return False
        y //= x

    return True

x = 10
y = 1
print(is_power(x, y))