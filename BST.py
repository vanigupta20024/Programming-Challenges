'''
Operations performed on BST:

Insert a node in bst
Search a node in bst
Find successor
Inorder traversal
Delete a node in bst:
    a. leaf
    b. one child
    c. both child
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
def inorder(root):
    
    if root == None: return 
    inorder(root.lchild)
    print(root.data, end = " ")
    inorder(root.rchild)
    
def search(root, key):
    
    if root is None or root.data == key:
        return root
    
    if key < root.data:
        return search(root.lchild, key)
    elif key > root.data:
        return search(root.rchild, key)
    
def succ(root):
    while root.left:
        root = root.left
    return root
    
def insert(root, key):
    
    if root == None:
        return Node(key)
    if key < root.data:
        root.lchild = insert(root.lchild, key)
    elif key > root.data:
        root.rchild = insert(root.rchild, key)
    return root

def delete(root, key):
    parent = curr = root
    while curr and curr.data != key:
        parent = curr
        if key < curr.data:
            curr = curr.lchild
        elif key > curr.data:
            curr = curr.rchild
    
    #if curr is none -> node not found
    if curr is None:
        return root
        
    #no child -> leaf
    if curr.lchild is None and curr.rchild is None:
        if curr != root:
            if curr == parent.lchild:
                parent.lchild = None
            else:
                parent.rchild = None
        else:
            root = None
    
    #1 child of node
    elif curr.lchild and not curr.rchild or curr.rchild and not curr.lchild:
        child = curr.lchild if curr.lchild else curr.rchild
        
        if curr != root:
            if parent.lchild == curr:
                parent.lchild = child
            else:
                parent.rchild = child
        else:
            root = child
    
    #2 childern
    else:
        new_val = succ(curr.right).data
        delete(root, new_val)
        curr.data = new_val
    return root

if __name__ == '__main__':
    
    root = None
    tree_data = [15, 10, 20, 8, 12, 18, 25]
    
    for val in tree_data:
        root = insert(root, val)
    
    inorder(root)
    print()
    deleted = delete(root, 18)
    inorder(root)
