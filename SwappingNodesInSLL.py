'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
Eg.
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length, curr = 1, head
        while curr:
            length += 1
            curr = curr.next
        length -= k
        v1, v2 = head, head
        while length > 1:
            length -= 1
            v1 = v1.next
        while k > 1:
            k -= 1
            v2 = v2.next
        v1.val, v2.val = v2.val, v1.val
        return head
