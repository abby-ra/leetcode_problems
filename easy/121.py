class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_prof = prices[0]
        max_prof = 0

        for i in range(1,len(prices)):
            min_prof = min(min_prof, prices[i])
            profit = prices[i] - min_prof
            max_prof = max(max_prof, profit)

        return max_prof
                    