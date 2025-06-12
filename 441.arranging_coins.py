class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right is the max number of complete rows







class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 0
        while n >= row + 1:
            row += 1
            n -= row
        return row
