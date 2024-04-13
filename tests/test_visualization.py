
import unittest
from visualization import Visualization


class TestVisualization(unittest.TestCase):
    def setUp(self):
        data = {
            'LAT': [40.7128, 40.7128, 41.8781],
            'LON': [-74.0060, -74.00601, -87.6298],
            '2006': 'value1',
            '2007': 'value2',
            '2008': 'value3',
            '2009': 'value4'
        }
        self.visual1 = Visualization(data)

    def test_generate_sub_keylist(self):
        result = self.visual1.generate_sub_keylist(2)
        self.assertEqual(result, ['2006', '2007', '2008', '2009'])

    def test_generate_sub_valuelist(self):
        result = self.visual1.generate_sub_valuelist(3)
        self.assertEqual(result, ['value2', 'value3', 'value4'])

    def test_draw_grpah(self):
        self.visual1.draw_grpah()
        self.assertIn('<div id=', self.visual1.result)  # Check that the result is a Plotly div

if __name__ == '__main__':
    unittest.main()