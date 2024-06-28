import unittest
import logging
from utils.logging_config import setup_logging

class TestLoggingConfig(unittest.TestCase):
    def test_logging_setup(self):
        setup_logging()
        logger = logging.getLogger(__name__)
        with self.assertLogs(logger, level='DEBUG') as log:
            logger.debug("Test log")
        self.assertIn("Test log", log.output[0])

if __name__ == '__main__':
    unittest.main()
