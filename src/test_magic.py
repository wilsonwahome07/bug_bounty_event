import unittest
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from magic_calculator import add, is_prime, show_secret


class TestMagic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(9))

    def test_secret_unlock(self):
        # Only show secret if all tests pass
        if self._outcome.success:
            show_secret()


if __name__ == "__main__":
    unittest.main()
