class Solution(object):
    def isMatch(self, s, p):
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                
                if j+1 < len(p) and p[j+1] == '*':
                    # Skip the "x*" pattern, or use one character if it matches
                    ans = dp(i, j+2) or (first_match and dp(i+1, j))
                else:
                    ans = first_match and dp(i+1, j+1)
            
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
