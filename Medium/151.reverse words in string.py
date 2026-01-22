class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return " ".join(words)
    


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         result = []
#         i = len(s) - 1

#         while i >= 0:
#             # skip spaces
#             while i >= 0 and s[i] == ' ':
#                 i -= 1

#             if i < 0:
#                 break

#             # collect characters of a word
#             j = i
#             while j >= 0 and s[j] != ' ':
#                 j -= 1

#             result.append(s[j+1:i+1])
#             i = j

#         return " ".join(result)
