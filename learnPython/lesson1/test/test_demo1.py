import unittest
from lesson1.demo1 import add

class MyTestCase(unittest.TestCase):
    def test_add(self):
        x=3
        y=4
        z=add(x,y)
        self.assertEqual(z, 7,'method add test failed')

if __name__ == '__main__':
    unittest.main()
