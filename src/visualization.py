
import plotly.graph_objects as go
from plotly.offline import plot

class Visualization:
    def __init__(self, dict):
        self.dict = dict
        self.result = None


    def generate_sub_keylist(self, index):
        return list(self.dict.keys())[index:]

    def generate_sub_valuelist(self, index):
        return list(self.dict.values())[index:]

    def draw_grpah(self):
        keys = self.generate_sub_keylist(2)
        values = self.generate_sub_valuelist(2)
        # print(keys, values)
        fig = go.Figure(data=go.Scatter(x=keys, y=values))
        div_string = plot(fig, output_type='div')
        self.result = div_string
        # return div_string


