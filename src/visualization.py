
import plotly.graph_objects as go
from plotly.offline import plot

def draw_grpah(dict):
    keys = list(dict.keys())[2:]
    values = list(dict.values())[2:]
    print(keys, values)
    fig = go.Figure(data=go.Scatter(x=keys, y=values))
    div_string = plot(fig, output_type='div')
    return div_string


