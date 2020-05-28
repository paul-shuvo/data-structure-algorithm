class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.cur = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        node_pointer = self.head
        str_val = ''
        while node_pointer is not None:
            str_val += str(node_pointer.data)  + ','
            node_pointer = node_pointer.next
        return str_val[:-1]
    
    def add(self, data):
        node = Node(data)
        if self.head is None:
             self.head = node
             self.cur = self.head
        else:
            self.cur.next = node
            self.cur = self.cur.next
        self.length += 1

    def remove(self, value):
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return

        node_pointer = self.head
        while node_pointer.next is not None:
            if node_pointer.next.data == value:
                node_pointer.next = node_pointer.next.next
                # Check if the last element is removed or not
                # If it is the last element then assign the node_pointer
                # to the self.cur
                if node_pointer.next is None:
                    self.cur = node_pointer
                self.length -= 1
                return
            node_pointer = node_pointer.next

    def insert(self, index, value):
        if index > self.length:
            raise IndexError(f'index: {index} greater than the list length: {self.length}')
        node = Node(value)
        if index == 0:
            node_pointer = self.head
            self.head = node
            self.head.next = node_pointer
            self.length += 1
            return
        elif index == self.length:
            self.cur.next = node
            self.cur = self.cur.next
            self.length += 1
            return
        
        node_prev = self.head
        node_cur = self.head.next
        index_ = 1
        while node_cur.next is not None:
            if index_ == index:
                node_prev.next = node
                node_prev.next.next = node_cur
                self.length += 1
                return
            node_prev = node_cur
            node_cur = node_cur.next
            index_ += 1

# a = Node(5)
# print(a)

sll = SinglyLinkedList()
sll.add(10)
sll.add(7)
sll.add(2.689)
sll.add('Hello')
sll.insert(2,100)
print(sll)
# sll.add(12)
# print(sll)
# sll.remove(10)
# print(sll)
# sll.remove('Hello')
# print(sll)
# sll.remove(12)
# print(sll)
# sll.add('full')
# sll.add(45)
# sll.remove(46)
# print(sll)
# print(len(sll))
# print(sll.length)