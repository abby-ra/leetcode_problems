class Solution:
    def countOdds(self, low, high):
        count = (high - low) // 2
        if low % 2 != 0 or high % 2 != 0:
            count += 1
        return count
