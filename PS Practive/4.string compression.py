#String compression input:aaabb output:a3b2

from doctest import Example


def compress(word):
    comp_word = " "
    count = 1
    
    for i in range(1,len(word)):
        if word[i] == word[i-1]:
            count+=1
        else:
            comp_word += word[i-1] + str(count)
            count = 1

    comp_word += word[-1] + str(count)
    return comp_word
    
word = input("Enter a string to compress: ")
print("Compressed string is:", compress(word))


# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"] 
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"] Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# class Solution:
#     def compress(self,chars):
#         res = []

#         for i in chars:
#             if i not in res:
#                 count = chars.count(i)
#                 res.append(i)
#                 if count > 1:
#                     res.extend(list(str(count)))

#         chars[:len(res)] = res
#         return len(res)