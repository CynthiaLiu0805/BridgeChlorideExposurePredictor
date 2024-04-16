'''
This module includes the visualization for the result
'''
import plotly.graph_objects as go
from plotly.offline import plot

# This function turns the keys in the dictionary to a list and exclude certain initial ones
def generate_sub_keylist(dict, index):
    return list(dict.keys())[index:]

# This function turns the value in the dictionary to a list and exclude certain initial ones
def generate_sub_valuelist(dict, index):
    return list(dict.values())[index:]

# This function does the plotting for result. The first two values are excluded because they are the longitude and latitude.
def draw_graph(dic):
    long = dic.get('LON')
    lat = dic.get('LAT')
    Year = generate_sub_keylist(dic,2)
    Chloride_exposure_values = generate_sub_valuelist(dic, 2)
    Chloride_exposure_values = [round(float(elem), 2) for elem in Chloride_exposure_values ]
    
    fig = go.Figure(data=go.Scatter(x=Year, y=Chloride_exposure_values))
    fig.update_layout(
    title=dict(
        text="Chloride exposure data on bridge corrosion at (" + lat[:5] + ", " + long[:5] + ")"
    ),
    xaxis_title=dict(text='Year'),
    yaxis_title=dict(text='Chloride exposure rate(kg/m^3)')
    )

    div_string = plot(fig, output_type='div')
    return div_string


