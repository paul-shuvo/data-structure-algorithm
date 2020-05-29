class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.length = 0
    
    def is_empty(self):
        return True if self.length == 0 else False
    
    def is_full(self):
        return True if self.length == self.size else False
    
    def push(self, data):
        if self.is_full():
            raise IndexError('Stack is full')
        node = Node(data)
        
        node.next = self.head
        self.head = node
        