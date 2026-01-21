def day_of_week(d, m, y):
    # Month offsets (March-based)
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if m < 3:
        y -= 1

    return (y + y//4 - y//100 + y//400 + t[m-1] + d) % 7
