# Python program to Digital Root (repeated digital sum) of the given large integer

# using mathematical formula

def singleDigit(n):
  
    # If given number is zero its
    # digit sum will be zero only
    if n == 0: 
        return 0
    
    # If result of modulo operation is 
    # zero then, the digit sum is 9
    if n % 9 == 0:
        return 9
    
    return n % 9

if __name__ == "__main__":
    n = 1234
    print(singleDigit(n))


# Examples :
# Input : num = "1234"
# Output : 1
# Explanation : The sum of 1+2+3+4 = 10, digSum(x) == 10,Hence ans will be 1+0 = 1

# Input : num = "5674"
# Output : 4 

