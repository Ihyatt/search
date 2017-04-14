import unittest
import challenge

class TestOnSearch(unittest.TestCase):
    """Class to test success and failures of methods"""

    def setUp(self):
        #creates instance of Search class from challenge module
        unittest.TestCase.setUp(self)
        self.test = challenge.Search()

    def test_less_than(self):
        #tests success and failure of less_than function within Search class
        assert challenge.Search.less_than(self.test, [0, 2, 4, 6, 8], 0) == 'NotFound'
        assert challenge.Search.less_than(self.test, [8, 6, 4, 2, 0],-1) == 'NotFound'
        assert challenge.Search.less_than(self.test, [8, 6, 4, 2, 0], 0) == 'NotFound'
        assert challenge.Search.less_than(self.test, [8, 6, 4, 2, 0], 3) == ('FoundLess', '3')
        assert challenge.Search.less_than(self.test, [8, 6, 4, 2, 0], 0) != ('FoundLess', '4')


    def test_less_than_equals(self):
        #tests success and failure of less_than_equals function within Search class
        assert challenge.Search.less_than_equals(self.test, [0, 2, 4, 6, 8], -1) == 'NotFound'
        assert challenge.Search.less_than_equals(self.test, [8, 6, 4, 2, 0], 4) == ('FoundExact', '2')
        assert challenge.Search.less_than_equals(self.test, [8, 6, 4, 2, 0], 3) == ('FoundLess', '3')
        assert challenge.Search.less_than_equals(self.test, [8, 6, 4, 2, 0], 3) != 'NotFound'

    def test_equals(self):
        #tests success and failure of equals function within Search class
        assert challenge.Search.equals(self.test, [0, 2, 4, 6, 8], 0) == ('FoundExact', '0')
        assert challenge.Search.equals(self.test, [0, 2, 4, 6, 8], 1) == 'NotFound'
        assert challenge.Search.equals(self.test, [0, 2, 4, 6, 8], 1) == 'NotFound'
        assert challenge.Search.equals(self.test, [0, 2, 4, 6, 8], 4) != 'NotFound'

    def test_greater_than_equals(self):
        #tests success and failure of greater_than_equals function within Search class
        assert challenge.Search.greater_than_equals(self.test, [0, 2, 4, 6, 8], 2) == ('FoundExact', '1')
        assert challenge.Search.greater_than_equals(self.test, [8, 6, 4, 2, 0], 5) == ('FoundGreater', '1')
        assert challenge.Search.greater_than_equals(self.test, [8, 6, 4, 2, 0], 2) == ('FoundExact', '3')
        assert challenge.Search.greater_than_equals(self.test, [8, 6, 4, 2, 0], 3) != 'NotFound'

    def test_greater_than(self):
         #tests success and failure of greater_than function within Search class
        assert challenge.Search.greater_than(self.test, [0, 2, 4, 6, 8], 2) == ('FoundGreater', '2')
        assert challenge.Search.greater_than(self.test, [8, 6, 4, 2, 0], 8) == 'NotFound'
        assert challenge.Search.greater_than(self.test, [8, 6, 4, 2, 0], 9) == 'NotFound'
        assert challenge.Search.greater_than(self.test, [8, 6, 4, 2, 0], 1) != 'NotFound'

  

if __name__ == '__main__':
    unittest.main()
    