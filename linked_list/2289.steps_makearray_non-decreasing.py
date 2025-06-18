class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []  # Each item is (num, steps)
        max_steps = 0

        for num in nums:
            steps = 0
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])
            if stack:
                steps += 1
            else:
                steps = 0
            stack.append((num, steps))
            max_steps = max(max_steps, steps)

        return max_steps
