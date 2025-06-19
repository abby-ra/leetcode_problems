class Solution(object):
    def isPalindrome(self, s):
    
        c = ""
        for char in s:
            if char.isalnum():            
                c += char.lower()  

        if c == c[::-1]:
            return True
        else:
            return False
