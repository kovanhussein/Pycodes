import unittest
from utils.utilities import greet, calculate_area

class TestUtilities(unittest.TestCase):
    def test_greet(self):
        with self.assertLogs(level='INFO') as log:
            greet('Alice')
        self.assertIn('Hello, Alice!', log.output[0])

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(5), 78.53981633974483)

if __name__ == '__main__':
    unittest.main()
