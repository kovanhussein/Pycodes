from utils.custom_data_structures import Stack, Queue, LinkedList, BinaryTree
from utils.decorators import log_decorator, repeat
from utils.error_handling import process_data, CustomError
from utils.logging_config import setup_logging
from utils.file_operations import read_file, write_file
from utils.api_requests import fetch_data
from utils.utilities import greet, calculate_area

import logging

# Setup logging
setup_logging()

#Logger instance
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting the main program")

    #Custom Data Structures
    stack= Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())

    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.display()

    binary_tree = BinaryTree()
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.inorder_traversal()

    # Decorators
    greet("Alice")  # Output with logging decorator
    repeated_greet = repeat(3)(greet)
    repeated_greet("Bob")  # Output with repeat decorator

    # Error Handling
    try:
        process_data(-5)
    except CustomError as e:
        logger.error(e)

    # File Operations
    write_file("example.txt", "Hello, World!")
    content = read_file("example.txt")
    print(content)  # Output: Hello, World!

    # API Requests
    data = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
    print(data)

    # Utility Functions
    area = calculate_area(5)
    print(area)  # Output: Area of the circle

    logger.info("Ending the main program")

if __name__ == "__main__":
    main()
