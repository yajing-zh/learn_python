import unittest
from lesson2.sortdemo import mysort

class MyTestCase(unittest.TestCase):
    def test_mysort1(self):
        x=[5,2,-1,10,7,4,8,-3]
        y1= mysort(x, 'abs', True)
        z1=[10, 8, 7, 5, 4, 3, 2, 1]
        self.assertEqual(y1==z1,True,'method mysort1 test failed')

    def test_mysort2(self):
        x = [5, 2, -1, 10, 7, 4, 8, -3]
        y2 = mysort(x, 'abs', False)
        z2=[1, 2, 3, 4, 5, 7, 8, 10]
        self.assertEqual(y2 == z2, True, 'method mysort2 test failed')


    def test_mysort3(self):
        x = [5, 2, -1, 10, 7, 4, 8, -3]
        y3 = mysort(x, 'sort', True)
        z3 = [10, 8, 7, 5, 4, 2, -1, -3]
        self.assertEqual(y3 == z3, True, 'method mysort3 test failed')

    def test_mysort4(self):
        x = [5, 2, -1, 10, 7, 4, 8, -3]
        y4 = mysort(x, 'sort', False)
        z4 = [-3, -1, 2, 4, 5, 7, 8, 10]
        self.assertEqual(y4 == z4, True, 'method mysort4 test failed')



if __name__ == '__main__':
    unittest.main()
