# Josephus Problem

def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n-1, k) + k) % n

# Input
N = int(input("Enter N: "))
k = int(input("Enter k: "))

# Survivor (1-based)
survivor = josephus(N, k) + 1
print(f"The survivor is at position: {survivor}")
