from data_structures.linkedlist import SinglyLinkedList
import pytest

def test_init():
    with pytest.raises(TypeError):
        sll = SinglyLinkedList(5)