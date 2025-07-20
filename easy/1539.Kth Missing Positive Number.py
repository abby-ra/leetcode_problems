class Solution:
    def findKthPositive(self, arr, k):
        num = 1
        missing = []

        i = 0
        while len(missing) < k:
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                missing.append(num)
            num += 1

        return missing[-1]
