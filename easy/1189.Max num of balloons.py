from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text) :
        # Count letters in text
        text_count = Counter(text)
        
        # Count letters in 'balloon'
        balloon_count = Counter("balloon")
        
        # For each letter in 'balloon', find how many times it can be formed
        return min(text_count[char] // balloon_count[char] for char in balloon_count)
