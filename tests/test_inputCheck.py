import unittest
from inputCheck import InputCheck
import inputCheck

class TestInputCheck(unittest.TestCase):

    # set up the test
    def setUp(self):
        self.test1 = InputCheck('123.45', 'abc')
        self.test2 = InputCheck('', '-123.3656')
        self.test3 = InputCheck('-80.84538', '44.550356')
        self.test4 = InputCheck('280.84538', '44.550356')
        self.test5 = InputCheck('277.4771', '42.63238')
        self.test6 = InputCheck('-123.3656', '48.4284')
        
    def test_load_file(self):
        # s = 'ontario_boundary.geojson'
        result = self.test1.load_file()
        self.assertIsNotNone(result)

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