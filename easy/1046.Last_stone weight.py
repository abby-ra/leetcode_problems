import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Use a max heap (invert values for heapq)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0
