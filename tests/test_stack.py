# from __future__ import absolute_import
from data_structures.stack import Stack
import pytest

def test_init():
    with pytest.raises(TypeError):
        stk = Stack(5, 0)
        
        stk = Stack(5)
        assert stk.size == 5
        
def test_is_empty():
    stk = Stack(0)
    
    assert stk.is_empty() == True
    
def test_is_full():
    stk = Stack(5)
    
    assert stk.is_full() == False
    
def test_push():
    stk = Stack(0)
    with pytest.raises(IndexError):
        stk.push(5)
        
    stk = Stack(3) 
    stk.push(1)
    assert stk.head.data == 1
    
    stk.push(2)
    assert stk.head.data == 2
    assert stk.head.next.data == 1
    
    stk.push(3)
    assert stk.head.data == 3
    assert stk.head.next.data == 2
    assert stk.head.next.next.data == 1
    
    with pytest.raises(IndexError):
        stk.push(4)
        
def test_pop():
    stk = Stack(0)
    with pytest.raises(IndexError):
        stk.pop()
    
    stk = Stack(3)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.pop()
    stk.pop()
    assert stk.head.data == 1
    assert stk.length == 1
    
def test_str():
    stk = Stack(3)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    
    assert str(stk) == '3,2,1'
    
def test_peek():
    stk = Stack(5)
    stk.push(0)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    
    with pytest.raises(IndexError):
        stk.peek(5)
    
    assert stk.peek(0) == 0
    assert stk.peek(2) == 2
    assert stk.peek(4) == 4