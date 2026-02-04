# Input: nums = [3,1,2,4] Output: [2,4,3,1] 
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

 

class Solution:
    def sortArrayByParity(self, A):
        n = []
        a = []

        for i in A:
            if i%2 == 0:
                n.append(i)
            else:
                a.append(i)

        A[:len(n+a)] = n+a
        return n+a