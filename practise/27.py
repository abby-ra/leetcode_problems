# Python3 program to implement  Rat and Poisoned bottle Problem

import math

# Function to find the 
# minimum number of rats 
def minRats(n):
    
    return math.ceil(math.log2(n)); 

# Driver Code 

# Number of bottles 
n = 1025; 
print("Minimum ", end = "")
print(minRats(n), end = " ")
print("rat(s) are required")


# Examples:

# Input: N = 4
# Output: 2
# Explanation: The minimum number of rats needed to find the poisoned bottle among 4 bottles is 2, using binary representation.

# Input: N = 100
# Output: 7
# Explanation: Since 2⁷ = 128 can cover up to 100 bottles, a minimum of 7 rats is required for identification.

# Input: N = 1000
# Output: 10
# Explanation: The minimum number of rats required is 10, as 210 = 1024 can uniquely identify one poisoned bottle among 1000.

