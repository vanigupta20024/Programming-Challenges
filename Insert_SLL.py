# function inserts data x in front of list and returns new head 
def insertAtBegining(head,x):
    new_node = Node(x)
    new_node.next = head
    head = new_node
    return new_node

# function appends data x at the end of list and returns new head
def insertAtEnd(head,x):
    new_node = Node(x)
    if head is None:
        head = new_node
        return head
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = new_node
    tail = new_node
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
def printlist(head):
    while head:
        print(head.data, end = " ")
        head = head.next
    print()
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for i in range(0, len(nodes) - 1, 2):
            if nodes[i + 1] == 0:
                a.head = insertAtBegining(a.head, nodes[i])
            else:
                a.head = insertAtEnd(a.head, nodes[i])
        printlist(a.head)
        
