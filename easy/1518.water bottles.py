class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange
            total_drunk += new_bottles
            empty = empty % numExchange + new_bottles

        return total_drunk
