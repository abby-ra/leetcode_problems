# Function to generate all primes <= n using Sieve
def sieve(n):
    is_prime = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

# Input
n = int(input("Enter n: "))

primes = sieve(n)
prime_positions = set(sieve(len(primes)))  # prime indices (1-based)
super_primes = [primes[i-1] for i in range(1, len(primes)+1) if i in prime_positions]

print(*super_primes)
