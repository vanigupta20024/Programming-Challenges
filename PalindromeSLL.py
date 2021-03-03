'''
Check if a singly linked list is a palindrome or not.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        
        l, h = 0, len(stack) - 1
        while l < h:
            if stack[l] != stack[h]:
                return False
            l += 1
            h -= 1
        return True
