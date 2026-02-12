def prime_range(n):
for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            prime = False
        else:
            print(num)
            break

n = int(input())
prime_range(n)