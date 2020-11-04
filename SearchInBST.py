# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # iterative solution
        while root is not None:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            elif val == root.val:
                return root
        return None
# Recursive solution

#         if root is None or val == root.val:
#             return root
        
#         if val < root.val:
#             return self.searchBST(root.left, val)
#         elif val > root.val:
#             return self.searchBST(root.right, val)
