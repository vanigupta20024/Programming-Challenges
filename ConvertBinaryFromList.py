'''
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Example: 
1 --> 0 --> 1 --> 1 --> 0

Return the decimal value of the number in the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        while head is not None: 
            s += str(head.val)
            head = head.next
        s = s[::-1]
        i = 0
        ans = 0
        for binary in s:
            ans += int(binary) * (2 ** i)
            i += 1
        return ans
