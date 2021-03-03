'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = None
        if l1 == None: return l2
        elif l2 == None: return l1
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else: 
            head = ListNode(l2.val)
            l2 = l2.next
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                temp = ListNode(l1.val)
                cur.next = temp
                cur = temp
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                cur.next = temp
                cur = temp
                l2 = l2.next
        if l1 != None:
            cur.next = l1
        elif l2 != None:
            cur.next = l2
        return head
