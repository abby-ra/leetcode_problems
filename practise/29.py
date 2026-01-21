# Function to return gcd of a and b 
# Euler's Totient Function

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# A simple method to evaluate Euler Totient Function 
def etf(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

# Driver Code    
if __name__ == "__main__":
    n = 11
    print(etf(n))