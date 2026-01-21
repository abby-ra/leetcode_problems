def closest_num(a,b):
    q = a//b
    x = q*b
    y = (q+1)*b

    if abs(a-x) < abs(a-y):
        return x
    elif abs(a-x) > abs(a-y):
        return y
    else:
        return x if abs(x) < abs(y) else y



a=int(input("Enter num:"))
b=int(input("Enter num:"))
print(closest_num(a,b))