class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
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
    
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp_list = self.head
            self.head = node
            self.head.next = temp_list
        self.length += 1

    def remove(self, value):
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return

        node_prev = self.head
        node_cur = node_prev.next
        while node_cur is not None:
            if node_cur.data == value:
                node_prev.next = node_cur.next
                self.length -= 1
                return
            node_prev = node_cur
            node_cur = node_cur.next

    def insert_at(self, index, value):
        if index > self.length:
            raise IndexError(f'index: {index} greater than the list length: {self.length}')
        node = Node(value)
        if index == 0:
            node_pointer = self.head
            self.head = node
            self.head.next = node_pointer
            self.length += 1
            return
        
        node_prev = self.head
        node_cur = node_prev.next
        index_ = 1
        while node_cur is not None:
            if index_ == index:
                node_prev.next = node
                node_prev.next.next = node_cur
                self.length += 1
                return
            node_prev = node_cur
            node_cur = node_cur.next
            index_ += 1
        node_prev.next = node
        self.length += 1
    
    def remove_from(self, index):
        if index >= self.length:
            raise IndexError(f'index: {index} greater than the list length: {self.length}')

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        node_prev = self.head
        node_cur = node_prev.next
        index_ = 1
        while node_cur is not None:
            if index_ == index:
                node_prev.next = node_cur.next
                self.length -= 1
                return
            node_prev = node_cur
            node_cur = node_cur.next
            index_ += 1


# a = Node(5)
# print(a)

# sll = SinglyLinkedList()
# sll.add(10)
# sll.add(7)
# sll.add(2.689)
# sll.add('Hello')
# sll.insert(2,100)
# print(sll)
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