class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue  # skip duplicates
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        nums.sort()  # sort to handle duplicates
        res = []
        used = [False] * len(nums)
        backtrack([], used)
        return res
