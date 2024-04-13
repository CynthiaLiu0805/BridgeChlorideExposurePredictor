
import unittest
from visualization import Visualization


class TestVisualization(unittest.TestCase):
    def setUp(self):
        data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'key4': 'value4'
        }
        self.visual1 = Visualization(data)

    def test_generate_sub_keylist(self):
        result = self.visual1.generate_sub_keylist(2)
        self.assertEqual(result, ['key3', 'key4'])

    def test_generate_sub_valuelist(self):
        result = self.visual1.generate_sub_valuelist(1)
        self.assertEqual(result, ['value2', 'value3', 'value4'])

    def test_draw_grpah(self):
        self.visual1.draw_grpah()
        self.assertIn('<div id=', self.visual1.result)  # Check that the result is a Plotly div

if __name__ == '__main__':
    unittest.main()