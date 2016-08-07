import unittest
from lesson1.sigmod import sigmod

class MyTestCase(unittest.TestCase):
    def test_sigmod(self):
        x=0
        y=sigmod(x)
        self.assertEqual(y,0.5, 'Method sigmod failed')

if __name__ == '__main__':
    unittest.main()
