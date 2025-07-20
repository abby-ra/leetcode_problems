class Solution:
    def sumOddLengthSubarrays(self, arr):
        total = 0
        n = len(arr)

        for length in range(1, n + 1, 2):  # only odd lengths
            for i in range(n - length + 1):  # start index
                subarray = arr[i:i + length]
                total += sum(subarray)

        return total
