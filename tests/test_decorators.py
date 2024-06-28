import unittest
from utils.decorators import log_decorator, repeat

class TestDecorators(unittest.TestCase):
    def test_log_decorator(self):
        @log_decorator
        def sample_function():
            return "Decorated!"

        self.assertEqual(sample_function(), "Decorated!")

    def test_repeat_decorator(self):
        @repeat(3)
        def sample_function():
            print("Repeated")

        with self.assertLogs(level='INFO') as log:
            sample_function()
        self.assertEqual(log.output.count("Repeated"), 3)

if __name__ == '__main__':
    unittest.main()
