# coding:utf-8
"""
@author:Yang Fan
@个人网站:https://heroyf.club
"""
class Array(object):
    def __init__(self, size=10):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head%self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('queue empty')
        value = self.array[self.tail%self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail

def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as execinfo:
        q.push(size)

    assert "full" in str(execinfo.value)

    assert len(q) == size
    assert q.pop() == 0
    assert q.pop() == 1
    q.push(5)
    assert len(q) == 4
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0

    with pytest.raises(EmptyError) as execinfo:
        q.pop()

    assert "empty" in str(execinfo.value)



