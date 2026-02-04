#odd palindromic numbers between two ranges input:10 and 20 output:(11,) input:10 and 40 output:(11,33)

def palin(n1,n2):
    palin = []

    for i in range(n1,n2+1):
        if str(i) == str(i)[::-1]:
            palin.append(i)

    return tuple(palin)

n1 = int(input("Enter first range: "))
n2 = int(input("Enter second range: "))
print(tuple(palin(n1,n2)))