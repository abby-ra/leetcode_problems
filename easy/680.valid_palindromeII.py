# class Solution:
#     def validPalindrome(self, s):
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             if s[left] != s[right]:
#                 # Try removing one character from either end
#                 skip_left = s[left+1:right+1]
#                 skip_right = s[left:right]
#                 return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
#             left += 1
#             right -= 1

#         return True


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(4)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

l3 = Node(0)

r = l3

cur = l1
while cur is not None:
    r.next = cur
    r = r.next
    cur = cur.next

cur = l2
while cur is not None:
    r.next = cur
    r = r.next
    cur = cur.next

cur =l3.next
while cur is not None:
    print(cur.data)
    cur = cur.next