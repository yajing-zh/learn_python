import unittest
from lesson3.day import week_of_date


class MyTestCase(unittest.TestCase):
    def test_day(self):
        year = 2016
        month = 7
        result= week_of_date(int(year), int(month))

        year1 = 2000
        month1 = 2
        result1 = week_of_date(int(year1), int(month1))

        self.assertEqual(result==0 and result1==2,True,'method day test failed')

if __name__ == '__main__':
    unittest.main()
