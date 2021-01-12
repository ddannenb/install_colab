import unittest
from an_api import AnApi

class MyTestCase(unittest.TestCase):
    def test_something(self):
        aa = AnApi("World")
        aa.do_something(True)

if __name__ == '__main__':
    unittest.main()
