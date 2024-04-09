import unittest
from input_check import Input_check

class TestInput_check(unittest.TestCase):

    # set up the test
    def setUp(self):
        self.test1 = Input_check('123.45', 'abc')
        self.test2 = Input_check('', '-123.3656')
        self.test3 = Input_check('-80.84538', '44.550356')
        self.test4 = Input_check('280.84538', '44.550356')
        self.test5 = Input_check('277.4771', '42.63238')
        self.test6 = Input_check('-123.3656', '48.4284')
        
    def test_load_file(self):
        # s = 'ontario_boundary.geojson'
        self.test1.load_file()
        self.assertIsNotNone(self.test1.boundary)

    def test_value_error(self):
        # latitude = "abc"
        # longitude = -123.3656
        with self.assertRaises(ValueError):
            self.test1.convert_latitude()
            
    def test_value_error_empty(self):
        # latitude = ""
        # longitude = -123.3656
        with self.assertRaises(ValueError):
            self.test2.convert_longitude()
    
    def test_point_in_boundary1(self):
        # latitude = 44.550356
        # longitude = -80.84538
        result = self.test3.is_within_ontario()
        self.assertTrue(result)

    def test_point_in_boundary2(self):
        latitude = 44.550356
        longitude = 280.84538
        result = self.test4.is_within_ontario()
        self.assertTrue(result)

    def test_point_not_in_boundary1(self):
        latitude = 42.63238
        longitude = 277.4771
        result = self.test5.is_within_ontario()
        self.assertFalse(result)

    def test_point_not_in_boundary2(self):
        latitude = 48.4284
        longitude = -123.3656
        result = self.test6.is_within_ontario()
        self.assertFalse(result)
    

if __name__ == '__main__':
    unittest.main()