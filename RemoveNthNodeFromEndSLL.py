'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Eg.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        index = length - n
        if index == 0:
            head = head.next
            return head
        cur = head
        prev = None
        while index != 0 and cur:
            prev = cur
            cur = cur.next
            index -= 1
        prev.next = cur.next
        return head
