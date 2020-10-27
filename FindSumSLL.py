# Brute force
def countPair(h1,h2,n1,n2,x):
    '''
    h1:  head of linkedList 1
    h2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:   len of linkedList 1
    X:   given sum
    '''
    
    count = 0
    head = h2
    while h1 is not None:
        while head is not None:
            if h1.data + head.data == x:
                count += 1
                head = head.next
            else:
                head = head.next
        if head is None:
            head = h2
            h1 = h1.next
            
    return count

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

                
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        X=int(input())
        
        
        print(countPair(ll1.head,ll2.head,n1,n2,X))

