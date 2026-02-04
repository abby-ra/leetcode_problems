#multiple of 2,in  triangle pattern 

def pattern(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(2*j, end = " ")
            #print(end=" ")
        print()



n = int(input())
print(pattern(n))