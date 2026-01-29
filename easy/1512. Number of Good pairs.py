from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = defaultdict(int)
        good_pairs = 0

        for num in nums:
            good_pairs += count[num]  # all previous occurrences make good pairs
            count[num] += 1           # update count

        return good_pairs
