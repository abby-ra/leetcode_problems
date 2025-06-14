class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        radius = 0
        
        def find_closest_heater(house):
            # Binary search to find the closest heater to the house
            left, right = 0, len(heaters) - 1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            # After loop:
            # heaters[right] < house < heaters[left] (or out of bounds)
            dist1 = abs(house - heaters[right]) if right >= 0 else float('inf')
            dist2 = abs(heaters[left] - house) if left < len(heaters) else float('inf')
            return min(dist1, dist2)
        
        for house in houses:
            closest_dist = find_closest_heater(house)
            radius = max(radius, closest_dist)
        
        return radius
 