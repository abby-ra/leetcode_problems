class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def process(n):
            stack = []

            for i in n:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack

        return process(s) == process(t)        