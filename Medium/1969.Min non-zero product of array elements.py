class Solution(object):
    def minNonZeroProduct(self, p):
        MOD = 10**9 + 7
        max_val = (1 << p) - 1            # 2^p - 1
        second_max = max_val - 1          # 2^p - 2
        exp = (1 << (p - 1)) - 1          # 2^(p-1) - 1
        
        power = pow(second_max, exp, MOD)
        return (power * max_val) % MOD
