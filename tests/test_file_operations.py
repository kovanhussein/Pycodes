import unittest
import os
from utils.file_operations import read_file, write_file

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'test_file.txt'

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_write_file(self):
        write_file(self.test_filename, 'Hello, World!')
        self.assertTrue(os.path.exists(self.test_filename))

    def test_read_file(self):
        write_file(self.test_filename, 'Hello, World!')
        content = read_file(self.test_filename)
        self.assertEqual(content, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
