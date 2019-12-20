from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.length += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.storage.length > 0:
            self.storage.length -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.storage.length
