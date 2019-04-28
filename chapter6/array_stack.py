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


class Array_Stack(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array_stack = Array(maxsize)
        self.head = 0
        self.tail = 0
        self.flag = 0

    def push(self, value):
        if len(self) > self.maxsize:
            raise FullError('queue full')
        self.array_stack[self.head%self.maxsize] = value
        self.head += 1
        self.tail = self.head


    def pop(self):
        if len(self) <= 0:
            raise EmptyError('queue empty')
        value = self.array_stack[self.tail-1]
        self.tail -= 1
        self.head = self.tail
        return value

    def __len__(self):
        return self.head - self.flag

def test_array_stack():
    size = 5
    s =  Array_Stack(size)
    for i in range(size):
        s.push(i)

    assert len(s) == 5
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
    assert len(s) == 0