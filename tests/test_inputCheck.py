import unittest
import inputCheck

class TestInputCheck(unittest.TestCase):
    def test_load_file1(self):
        s = 'ontario_boundary.geojson'
        result = inputCheck.load_file(s)
        self.assertIsNotNone(result)

    def test_load_file2(self):
        s = 'boundary.geojson'
        with self.assertRaises(FileNotFoundError):
            inputCheck.load_file(s)

    def test_is_float1(self):
        s = "123.45"
        result = inputCheck.is_float(s)
        self.assertTrue(result)

    def test_value_error(self):
        latitude = "abc"
        # longitude = -123.3656
        with self.assertRaises(ValueError):
            inputCheck.inputCheck(latitude)
            
    def test_value_error_empty(self):
        latitude = ""
        # longitude = -123.3656
        with self.assertRaises(ValueError):
            inputCheck.inputCheck(latitude)
    
    def test_point_in_boundary1(self):
        latitude = 44.550356
        longitude = -80.84538
        result = inputCheck.is_within_ontario(latitude, longitude)
        self.assertTrue(result)

    def test_point_in_boundary2(self):
        latitude = 44.550356
        longitude = 280.84538
        result = inputCheck.is_within_ontario(latitude, longitude)
        self.assertTrue(result)

    def test_point_not_in_boundary1(self):
        latitude = 42.63238
        longitude = 277.4771
        result = inputCheck.is_within_ontario(latitude, longitude)
        self.assertFalse(result)

    def test_point_not_in_boundary2(self):
        latitude = 48.4284
        longitude = -123.3656
        result = inputCheck.is_within_ontario(latitude, longitude)
        self.assertFalse(result)
    

if __name__ == '__main__':
    unittest.main()