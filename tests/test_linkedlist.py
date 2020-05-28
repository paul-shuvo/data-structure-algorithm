from data_structures.linkedlist import SinglyLinkedList
import pytest

def test_init():
    with pytest.raises(TypeError):
        sll = SinglyLinkedList(5)
        

def test_insert():
    sll = SinglyLinkedList()
    sll.insert(5)
    assert sll.head.data == 5
    
    sll.insert('Hello')
    assert  sll.head.data == 'Hello'
    
    sll.insert('World')
    assert  sll.head.data == 'World'
    assert  sll.head.next.data == 'Hello'
    
def test_remove():
    sll = SinglyLinkedList()
    sll.insert('Hello')
    sll.insert('World')
    sll.insert(10)
    
    sll.remove(10)
    assert sll.head.data == 'World'
    
    sll.insert(100)
    sll.remove('Hello')
    assert sll.length == 2
    
    
def test_insert_at():
    sll = SinglyLinkedList()
    sll.insert(0)
    assert sll.head.data == 0
    
    with pytest.raises(IndexError):
        sll.insert_at(2, 8)
        
    sll.insert(5)   
    sll.insert_at(0,2)
    assert sll.head.data == 2
    
    sll.insert_at(sll.length, 10)
    assert sll.head.next.next.next.data == 10
    
    # sll.insert(3, 20)
    # ass
    
def test_remove_at():
    sll = SinglyLinkedList()
    sll.insert(0)
    assert sll.head.data == 0
    
    with pytest.raises(IndexError):
        sll.remove_from(sll.length)
    
    sll.remove_from(0)
    assert sll.head == None
    
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4)
    sll.remove_from(0)
    assert sll.head.data == 3
    
    sll.insert(4)
    sll.remove_from(1)
    assert str(sll) == '4,2,1'
    
    sll.remove_from(2)
    assert str(sll) == '4,2'
    assert sll.head.next.next is None

def test_find():
    sll = SinglyLinkedList()
    assert sll.find(10) == -1
    
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4)
    
    assert sll.find(3) == 1
    assert sll.find(10) == -1

def test_find_at():
    sll = SinglyLinkedList()
    with pytest.raises(IndexError):
        sll.find_at(0)
    
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4)
    
    assert sll.find_at(3) == 1
    assert sll.find_at(0) == 4

    with pytest.raises(IndexError):
        assert sll.find_at(4)