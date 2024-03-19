
import plotly.graph_objects as go
from plotly.offline import plot

def generate_sub_keylist(dict, index):
    return list(dict.keys())[index:]

def generate_sub_valuelist(dict, index):
    return list(dict.values())[index:]

def draw_grpah(dict):
    keys = generate_sub_keylist(dict, 2)
    values = generate_sub_valuelist(dict, 2)
    # print(keys, values)
    fig = go.Figure(data=go.Scatter(x=keys, y=values))
    div_string = plot(fig, output_type='div')
    return div_string


