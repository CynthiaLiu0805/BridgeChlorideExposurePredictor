import unittest
from input_check import Input_check

class TestInput_check(unittest.TestCase):

    # set up the test
    def setUp(self):
        self.test1 = Input_check('123.45', 'abc')
        self.test2 = Input_check('', '-123.3656')
        self.test3 = Input_check('-79.07622', '43.26204')
        self.test4 = Input_check('280.84538', '44.550356')
        self.test5 = Input_check('277.4771', '42.63238')
        self.test6 = Input_check('-79.07264', '43.26259')
        
    def test_load_file(self):
        self.test1.load_file()
        self.assertIsNotNone(self.test1.boundary)

    def test_value_error_nonnumerical(self):
        with self.assertRaises(ValueError):
            self.test1.convert_latitude()
            
    def test_value_error_empty(self):
        with self.assertRaises(ValueError):
            self.test2.convert_longitude()
    
    def test_on_ontario_boundary(self):
        result = self.test3.is_within_ontario()
        self.assertTrue(result)

    def test_in_ontario_boundary(self):
        result = self.test4.is_within_ontario()
        self.assertTrue(result)

    def test_outside_ontario_boundary(self):
        result = self.test5.is_within_ontario()
        self.assertFalse(result)

    def test_lake_on_edge_of_ontario(self):
        result = self.test6.is_within_ontario()
        self.assertFalse(result)
    

if __name__ == '__main__':
    unittest.main()