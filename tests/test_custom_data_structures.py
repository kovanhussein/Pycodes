import unittest
from utils.custom_data_structures import Stack, Queue, LinkedList, BinaryTree

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

class TestLinkedList(unittest.TestCase):
    def test_append_display(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        # Capturing the display output
        with self.assertLogs(level='INFO') as log:
            linked_list.display()
        self.assertIn('1 -> 2 -> None', log.output[0])

class TestBinaryTree(unittest.TestCase):
    def test_insert_inorder_traversal(self):
        binary_tree = BinaryTree()
        binary_tree.insert(3)
        binary_tree.insert(1)
        binary_tree.insert(4)
        # Capturing the inorder traversal output
        with self.assertLogs(level='INFO') as log:
            binary_tree.inorder_traversal()
        self.assertIn('1 3 4', log.output[0])

if __name__ == '__main__':
    unittest.main()
