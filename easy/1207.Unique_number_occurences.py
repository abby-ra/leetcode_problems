class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter

        freq = Counter(arr)
        occurrences = list(freq.values())

        return len(occurrences) == len(set(occurrences))
