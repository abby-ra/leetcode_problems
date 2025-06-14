class Solution:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k  # possible starting points of k elements

        while left < right:
            mid = (left + right) // 2

            distLeft = x - arr[mid]
            distRight = arr[mid + k] - x

            # if left side is farther, move right
            if distLeft > distRight:
                left = mid + 1
            else:
                right = mid
        
        # Return the k elements starting from the best left position
        result = []
        for i in range(left, left + k):
            result.append(arr[i])
        return result
