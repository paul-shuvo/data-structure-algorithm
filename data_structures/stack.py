class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
        
class Stack:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        node = self.head
        retval = ""
        while node is not None:
            retval += str(node) + ','
            node = node.next
        return retval[:-1]
    
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
        self.length += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is full')
        self.head = self.head.next
        self.length -= 1
    
    def peek(self, index):
        if index >= self.length:
            raise IndexError(f'index: {index} greater than the stack length: {self.length}')
        count = self.length - 1
        node = self.head
        while count >= index:
            if count == index:
                return node.data
            count -= 1
            node = node.next
            
# stk = Stack(5)
# stk.push(1)
# stk.push("hee")
# stk.push(12.45)
# print(stk)
# # stk.push(stk)
# stk2 = Stack(3)
# stk2.push(5)
# stk2.push(stk)
# print(stk2)