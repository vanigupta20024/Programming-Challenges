'''
class Node:
    data=0
    left=None
    right=None

'''

def minValue(root):
    if root is None:
        return -1
    m = 0
    while root.left is not None:
        root = root.left
    return root.data
