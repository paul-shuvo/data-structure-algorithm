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

        pointer = self.head
        while pointer.next is not None:
            if pointer.next.data == value:
                pointer.next = pointer.next.next
                # Check if the last element is removed or not
                # If it is the last element then assign the pointer
                # to the self.cur
                if pointer.next is None:
                    self.cur = pointer
                self.length -= 1
                return
            pointer = pointer.next


    def __len__(self):
        return self.length

    def __str__(self):
        pointer = self.head
        str_val = ''
        while pointer is not None:
            str_val += str(pointer.data)  + ','
            pointer = pointer.next
        return str_val[:-1]

# a = Node(5)
# print(a)

# sll = SinglyLinkedList()
# sll.add(10)
# sll.add(7)
# sll.add(2.689)
# sll.add('Hello')
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