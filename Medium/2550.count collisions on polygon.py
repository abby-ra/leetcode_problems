class Solution(object):
    def monkeyMove(self, n):
        MOD = 10**9 + 7
        total = pow(2, n, MOD)  # total possible movements
        return (total - 2) % MOD
