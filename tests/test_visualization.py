import visualization
import plotly.graph_objects as go
from plotly.offline import plot
import unittest


class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'key4': 'value4'
        }

    def test_generate_sub_keylist(self):
        result = visualization.generate_sub_keylist(self.data, 2)
        self.assertEqual(result, ['key3', 'key4'])

    def test_generate_sub_valuelist(self):
        result = visualization.generate_sub_valuelist(self.data, 1)
        self.assertEqual(result, ['value2', 'value3', 'value4'])

    def test_draw_grpah(self):
        result = visualization.draw_grpah(self.data)
        self.assertIn('<div id=', result)  # Check that the result is a Plotly div

if __name__ == '__main__':
    unittest.main()