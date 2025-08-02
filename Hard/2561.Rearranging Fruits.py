from collections import Counter

class Solution:
    def minCost(self, basket1, basket2):
        count = Counter(basket1 + basket2)

        # Step 1: Check if possible
        for fruit, freq in count.items():
            if freq % 2 != 0:
                return -1  # not possible

        # Step 2: Count extra fruits in each basket
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        extra1 = []
        extra2 = []

        for fruit in count:
            diff = c1[fruit] - (count[fruit] // 2)
            if diff > 0:
                extra1.extend([fruit] * diff)
            elif diff < 0:
                extra2.extend([fruit] * (-diff))

        extra1.sort()
        extra2.sort(reverse=True)

        min_fruit = min(count)
        cost = 0

        # Step 3: Calculate minimal swap cost
        for x, y in zip(extra1, extra2):
            cost += min(min(x, y), 2 * min_fruit)

        return cost
