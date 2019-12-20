from dll_stack import Stack
from dll_queue import Queue
import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self
        finished = False
        while not finished:
            if current_node.value == value:
                return
            elif current_node.value < value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = BinarySearchTree(value)
                    finished = True
            elif current_node.value > value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = BinarySearchTree(value)
                    finished = True

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        current_node = self
        finished = False
        while not finished:
            if current_node.value == target:
                return True
            elif current_node.value < target:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    finished = True
            elif current_node.value > target:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    finished = True
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # current_node = self
        # while current_node.right:
        #     current_node = current_node.right
        # return current_node.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def traverse(node):
            if node:
                node.value = cb(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(self)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        def traverse(node):
            if node:
                traverse(node.left)
                print(node.value)
                traverse(node.right)
        traverse(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len():
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len():
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right is not None:
                stack.push(current_node.right)
            if current_node.left is not None:
                stack.push(current_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
