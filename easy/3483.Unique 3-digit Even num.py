from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        unique_nums = set()
        
        for p in permutations(digits, 3):
            if p[0] == 0:  # no leading 0
                continue
            if p[2] % 2 != 0:  # must be even
                continue
            num = p[0] * 100 + p[1] * 10 + p[2]
            unique_nums.add(num)
        
        return len(unique_nums)
