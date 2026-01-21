# Function to find the
# nth term of series
def term(n) :
    # Loop to add numbers
    ans = 0
    for i in range(1,n+1) :
        ans = ans + i 
     
    return ans


n = 4
print(term(n))