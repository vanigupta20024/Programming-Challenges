import sys
import io

def getCount(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next
        
if __name__ == "__main__":
    t = int(input())
    for cases in range(t):
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            node = Node(x)
            a.append(node)
        print(getCount(a.head))
