class Solution(object):
    def kthCharacter(self, k):
        word = ['a']  # start with 'a'
        
        while len(word) < k:
            next_letters = []
            for ch in word:
                if ch == 'z':
                    next_letters.append('a')
                else:
                    next_letters.append(chr(ord(ch) + 1))
            word += next_letters
        
        return word[k - 1]
