from search import Search
import unittest
import pandas as pd
import numpy as np
from flask import Flask


class TestInputCheck(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.search1 = Search(-73.935242, 40.730610)
        self.search2 = Search(274.7636, 49.67531)
        self.search1.data = pd.DataFrame({
            'LAT': [40.7128, 40.7128, 41.8781],
            'LON': [-74.0060, -74.00601, -87.6298]
        })
        self.search2.load_data()


    def test_load_data(self):
        self.search2.load_data()
        self.assertIsNotNone(self.search2.data)
    

    def test_find_closest_four_decimal(self):
        result = self.search1.find_closest()
        np.testing.assert_equal(result, 0)
        np.testing.assert_equal(result, 0)

    def test_find_closest_large_dataset(self):
        result = self.search2.find_closest()
        
        np.testing.assert_equal(result, 1)
        np.testing.assert_equal(result, 1)

if __name__ == '__main__':
    unittest.main()

