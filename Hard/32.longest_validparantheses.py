class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]  # Start with -1 to help calculate length
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop matching '('
                if not stack:
                    stack.append(i)  # New base index
                else:
                    max_len = max(max_len, i - stack[-1])  # Valid length

        return max_len
