class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        a = Counter(s)  # Count frequency of each character

        for i, ch in enumerate(s):
            if a[ch] == 1:
                return i
        return -1
