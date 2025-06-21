class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = []

        for i in range(n):
            found = False
            for j in range(1, n):  # check next n-1 elements in circular way
                next_index = (i + j) % n
                if nums[next_index] > nums[i]:
                    res.append(nums[next_index])
                    found = True
                    break
            if not found:
                res.append(-1)

        return res
