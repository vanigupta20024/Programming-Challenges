'''
Given a linked list, swap every two adjacent nodes and return its head.
Eg.
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        curr = head
        nxt = head.next
        while nxt:
            curr.val, nxt.val = nxt.val, curr.val
            if not nxt.next or not nxt.next.next:
                return head
            curr = nxt.next
            nxt = curr.next
        return head
