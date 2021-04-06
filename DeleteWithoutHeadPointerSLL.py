'''
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. 
The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you. It is guaranteed that the node to be deleted is not a tail node in the linked list.

Input:
N = 4
value[] = {10,20,4,30}
node = 20
Output: 10 4 30

Your Task:
You only need to complete the function deleteNode that takes reference to the node that needs to be deleted. The printing is done automatically by the driver code.

Expected Time Complexity : O(1)
Expected Auxilliary Space : O(1)
'''

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        curr_node.data = curr_node.next.data
        temp = curr_node.next
        if curr_node.next.next == None:
            curr_node.next = None
        else:
            curr_node.next = curr_node.next.next
        del temp
