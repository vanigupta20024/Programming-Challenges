
def length_even_odd(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return 1 if c % 2 == 0 else 0

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
    for _ in range(t):
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            new_node = Node(x)
            a.append(new_node)
            
        if length_even_odd(a.head) :
            print("Even")
        else :
            print("Odd")
        
        
