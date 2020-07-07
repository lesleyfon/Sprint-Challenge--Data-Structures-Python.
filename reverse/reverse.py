class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        stack = []
        if self.head is None:
            return

        while self.head is not None:
            stack.append(self.head.value)
            self.head = self.head.next_node

        for data in stack:
            self.add_to_head(data)


l = LinkedList()


def test_longer_reverse():
    l.add_to_head(1)
    l.add_to_head(2)
    l.add_to_head(3)
    l.add_to_head(4)
    l.add_to_head(5)
    print(l.head.value, 5)
    l.reverse_list(l.head, None)
    print(l.head.value, 1)
    print(l.head.get_next().value, 2)
    print(l.head.get_next().get_next().value, 3)


test_longer_reverse()
