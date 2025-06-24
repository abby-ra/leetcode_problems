class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse=True)  # Remove duplicates and sort descending
        if len(nums) >= 3:
            return nums[2]  # Third maximum
        else:
            return nums[0]  # Maximum
