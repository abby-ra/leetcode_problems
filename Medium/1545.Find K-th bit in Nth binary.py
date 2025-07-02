class Solution(object):
    def findKthBit(self, n, k):
        def helper(a, b):
            if a == 1:
                return '0'
            
            length = (1 << a) - 1  # 2^a - 1
            mid = (length // 2) + 1

            if b == mid:
                return '1'
            elif b < mid:
                return helper(a - 1, b)
            else:
                mirror_k = length - b + 1
                bit = helper(a - 1, mirror_k)
                return '1' if bit == '0' else '0'

        return helper(n, k)
