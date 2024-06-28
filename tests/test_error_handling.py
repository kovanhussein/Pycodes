import unittest
from utils.error_handling import process_data, CustomError

class TestErrorHandling(unittest.TestCase):
    def test_process_data_positive(self):
        self.assertEqual(process_data(10), 10)

    def test_process_data_negative(self):
        with self.assertRaises(CustomError):
            process_data(-1)

if __name__ == '__main__':
    unittest.main()
