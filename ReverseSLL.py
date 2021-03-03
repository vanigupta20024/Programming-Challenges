'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = None
        curr = nxt = head
        
        while nxt != None:
            nxt = nxt.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
     
# Recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverseLL(head, prev = None)
    
    def _reverseLL(self, head, prev = None):
        if not head:
            return prev
        node = head.next
        head.next = prev
        return self._reverseLL(node, head)
