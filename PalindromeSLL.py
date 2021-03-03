'''
Check if a singly linked list is a palindrome or not.
'''

# Time: O(n) Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None: return True
        slow = fast = head
        temp = None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            temp = slow
            slow = slow.next
        curr = nxt = slow
        prev = None
        while nxt != None:
            nxt = nxt.next
            curr.next = prev
            prev = curr
            curr = nxt
        temp.next = prev
        slow = temp.next
        while slow != None:
            if slow.val != head.val:
                print(slow.val, head.val)
                return False
            slow = slow.next
            head = head.next
        return True
        
# Time: O(N) Space: O(1)
#         stack = []
#         while head != None:
#             stack.append(head.val)
#             head = head.next
        
#         l, h = 0, len(stack) - 1
#         while l < h:
#             if stack[l] != stack[h]:
#                 return False
#             l += 1
#             h -= 1
#         return True
