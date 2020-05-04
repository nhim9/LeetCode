import collections

a = ["asdaf", "as", "asdsdfcd"]
#print(sorted(a, key = len, reverse=True))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Node(12)
node2 = Node(3)
node3 = Node(21)
node4 = Node(323)

node1.next = node2
node2.next = node3
node3.next = node4

def search_list(L, key):
    while L and L.val != key:
        L = L.next
    return L

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next

def merge_two_sorted_lists(L1, L2):
    dummy_head=tail=Node()
    while L1 and L2:
        if L1.val<L2.val:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next

#doubly linked list
class Node_double:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


node5 = Node_double(45)
node6 = Node_double(56)
node7 = Node_double(3)
node5.next, node6.next = node6, node7
node6.prev, node7.next = node5, node6

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))

def is_well_formed(s):
    left_chars = []
    lookup = {"(": ")", "{": "}", "[": "]"}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] !=c:
            return False
    return not left_chars

print(is_well_formed("()[{]}"))
