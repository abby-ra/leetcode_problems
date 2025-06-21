class Solution:
    def removeDuplicateLetters(self, s):
        last = {c: i for i, c in enumerate(s)}  # Last index of each character
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)

        return ''.join(stack)
