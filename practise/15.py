def rectanglesOverlap(l1, r1, l2, r2):
    # If one rectangle is on left side of the other
    if r1[0] <= l2[0] or r2[0] <= l1[0]:
        return False

    # If one rectangle is above the other
    if l1[1] <= r2[1] or l2[1] <= r1[1]:
        return False

    return True


if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if rectanglesOverlap(l1, r1, l2, r2):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")





# Each rectangle is axis-aligned and represented by:

# l1(x1, y1) → top-left of rectangle 1

# r1(x2, y2) → bottom-right of rectangle 1

# l2(x3, y3) → top-left of rectangle 2

# r2(x4, y4) → bottom-right of rectangle 2