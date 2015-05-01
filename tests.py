import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")

class TestAgain(unittest.TestCase):
    def test_some(self):
        self.assertEqual(awesome.frown(), ":(")


if __name__ == '__main__':
    unittest.main()
