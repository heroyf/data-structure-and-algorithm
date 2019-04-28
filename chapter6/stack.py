class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class CircualDoublelinkedlist(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev, node.next = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("full")
        node = Node(value=value)
        tailnode = self.root.prev

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node

        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("full")
        node = Node(value=value)

        if self.root.next is self.root:  # empth double_linked_list
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):  # O(1)
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

##############################################
# 实现栈
##############################################

class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class Deque(CircualDoublelinkedlist):
    def pop(self):
        if len(self) == 0:
            raise EmptyError('Queue Empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value


    def popleft(self):
        if len(self) == 0:
            raise EmptyError('Queue Empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


class Stack(object):
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert len(s) == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
    assert s.is_empty()

    import pytest
    with pytest.raises(EmptyError) as execinfo:
        s.pop()
    assert "Empty" in str(execinfo.value)




