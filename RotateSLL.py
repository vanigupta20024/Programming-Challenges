'''
Given the head of a linked list, rotate the list to the right by k places.
Eg.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        l = 0
        if not head or k == 0:
            return head
        curr = head
        while curr:
            l += 1
            curr = curr.next
        if k >= l: k %= l
        if k == 0: return head
        last, curr, prev = head, head, None
        while last.next:
            prev = last
            last = last.next
        last.next = head
        k = l - k
        while k:
            k -= 1
            prev = curr
            curr = curr.next
        prev.next = None
        return curr
