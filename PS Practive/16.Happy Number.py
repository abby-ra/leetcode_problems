
class Solution:
    def isHappy(self, n):
        seen = set()
        
        while n != 1:
            if n  in seen:
                return False
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))

        if n == 1:
            return "true"
        else:
            return "false"

