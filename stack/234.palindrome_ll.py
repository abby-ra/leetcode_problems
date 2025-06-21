class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        vals = []
        current = head

        # Step 1: Copy all values into a list
        while current:
            vals.append(current.val)
            current = current.next

        # Step 2: Check if the list is a palindrome
        return vals == vals[::-1]
