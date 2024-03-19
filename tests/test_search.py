import search
import unittest
import pandas as pd
import numpy as np
from flask import Flask


class TestInputCheck(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.data = pd.DataFrame({
            'LAT': [40.7128, 34.0522, 41.8781],
            'LON': [-74.0060, -118.2437, -87.6298]
        })

    def test_load_data1(self):
        s = 'data.csv'
        result = search.load_data(s)
        self.assertIsNotNone(result)
    
    def test_load_data2(self):
        s = 'd.csv'
        with self.assertRaises(FileNotFoundError):
            search.load_data(s)

    def test_find_closest1(self):
        lat = 40.730610
        lon = -73.935242
        result = search.find_closest(lat, lon, self.data)
        
        np.testing.assert_almost_equal(result['LAT'], 40.7128)
        np.testing.assert_almost_equal(result['LON'], -74.0060)

    def test_find_closest2(self):
        lat = 49.45
        lon = -85.23
        data = search.load_data('data.csv')
        result = search.find_closest(lat, lon, data)
        
        np.testing.assert_almost_equal(result['LAT'], 49.45781)
        np.testing.assert_almost_equal(result['LON'], 274.7127)

    def test_convert_lon_calculate1(self):
        lon = -74.0060
        result = search.convert_lon_calculate(lon)
        self.assertEqual(result, 285.994)
    
    def test_convert_lon_calculate2(self):
        lon = 274.7127
        result = search.convert_lon_calculate(lon)
        self.assertEqual(result, 274.7127)
   

    def test_search_coordinates(self):
        with self.app.test_request_context('/?latitude=40.7128&longitude=-74.0060'):
            result = search.search_coordinates()
            self.assertIn('40.7128', result)
            self.assertIn('-74.0060', result)

if __name__ == '__main__':
    unittest.main()

