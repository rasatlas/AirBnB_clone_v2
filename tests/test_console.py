import console
import unittest


class TestConsole(unittest.TestCase):
    """ test for the console """
    def test_module_doc(self):
        """ test for module doc """
        self.assertIsNotNone(console.__doc__)


if __name__ == "__main__":
    unittest.main()
