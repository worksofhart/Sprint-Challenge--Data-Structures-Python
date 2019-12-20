from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.position = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.position += 1
        if self.position > self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            # self.position = 1
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node is not None:
            if current_node.value is not None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        print(list_buffer_contents)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.position = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.position] = item
        self.position += 1
        if self.position == self.capacity:
            self.position = 0

    def get(self):
        return [x for x in self.storage if x is not None]

        # Trying out filter and lambda
        # return list(filter(lambda x: x is not None, self.storage))
