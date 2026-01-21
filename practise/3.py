
def nth(a,b,n):
    nths = a
    diff = b - a
    for i in range(1,n):
        nths += diff
    return nths



a = 2
b = 3
n = 4
print(nth(a,b,n))