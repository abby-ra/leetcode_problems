class solution(object):
    def majorityelement(self, nums):
        k = 0
        for num in nums:
            if k == 0 or nums[k-1] == num:
                nums[k] = num
                k+=1

        return k