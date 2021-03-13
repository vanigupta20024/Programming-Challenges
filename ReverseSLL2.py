'''
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next or left == right: return head
        curr, nxt = head, head.next
        prev = _left = None
        n = 0
        while left > 1:
            left -= 1
            n += 1
            prev, curr = curr, nxt
            nxt = nxt.next
        _left, start = prev, curr
        while n != right:
            n += 1
            curr.next = prev
            prev, curr = curr, nxt
            if nxt: nxt = nxt.next
        start.next = curr
        if _left == None: return prev
        _left.next = prev
        return head
