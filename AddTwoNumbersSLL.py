'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check_carry(self, carry, add):
        if add > 9: return 1, add % 10
        return 0, add
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1.next and l1.val == 0: return l2
        if not l2.next and l2.val == 0: return l1
        carry, head_l1 = 0, l1
        while l1 and l2:
            add_result = l1.val + l2.val + carry
            carry, add_result = self.check_carry(carry, add_result)
            if not carry: carry = 0
            l1.val = add_result
            l1, l2, prev = l1.next, l2.next, l1
        if not l1 and not l2:
            if carry != 0:
                l1 = ListNode(carry)
                prev.next = l1
            return head_l1
        if not l1:
            prev.next, prev = l2, l2
            if not carry: return head_l1
            while l2:
                add_result = l2.val + carry
                carry, add_result = self.check_carry(carry, add_result)
                l2.val = add_result
                if not carry: return head_l1
                prev, l2 = l2, l2.next
            if carry: prev.next = ListNode(carry)
            return head_l1
        if not l2:
            if not carry: return head_l1
            while l1:
                add_result = l1.val + carry
                carry, add_result = self.check_carry(carry, add_result)
                l1.val = add_result
                if not carry: return head_l1
                prev, l1 = l1, l1.next
            if carry: prev.next = ListNode(carry)
            return head_l1
