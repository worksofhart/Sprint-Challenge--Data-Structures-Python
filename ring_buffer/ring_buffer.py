from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If not at capacity yet, add item to the tail and set current position to the head
        if self.storage.length != self.capacity:
            self.current = self.storage.head
            self.storage.add_to_tail(item)
        # Else we're already at capacity
        else:
            # So overwrite the current node's value
            self.current.value = item
            # And if we're at the tail, we need to wrap back around to the head
            if self.current is self.storage.tail:
                self.current = self.storage.head
            # Otherwise update position to the next node
            else:
                self.current = self.current.next

    def get(self):
        list_buffer_contents = []
        current_node = self.storage.head

        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        return [x for x in self.storage if x is not None]

        # Trying out filter and lambda
        # return list(filter(lambda x: x is not None, self.storage))
