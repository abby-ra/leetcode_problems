class Solution(object):
    def predictTheWinner(self, nums):
        memo = {}

        def helper(a, b):
            if a == b:
                return nums[a]
            if (a, b) in memo:
                return memo[(a, b)]

            pick_left = nums[a] - helper(a + 1, b)
            pick_right = nums[b] - helper(a, b - 1)

            memo[(a, b)] = max(pick_left, pick_right)
            return memo[(a, b)]

        return helper(0, len(nums) - 1) >= 0
