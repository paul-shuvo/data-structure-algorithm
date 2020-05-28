from data_structures.linkedlist import SinglyLinkedList
import pytest

def test_init():
    with pytest.raises(TypeError):
        sll = SinglyLinkedList(5)
        
def test_insert():
    sll = SinglyLinkedList()
    sll.add(0)
    assert sll.head.data == 0
    
    with pytest.raises(IndexError):
        sll.insert(2, 8)
        
    sll.add(5)   
    sll.insert(0,2)
    assert sll.head.data == 2
    
    sll.insert(sll.length, 10)
    assert sll.cur.data == 10
    
    # sll.insert(3, 20)
    # ass