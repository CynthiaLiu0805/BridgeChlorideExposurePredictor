
import plotly.graph_objects as go
from plotly.offline import plot



def generate_sub_keylist(dict, index):
    return list(dict.keys())[index:]

def generate_sub_valuelist(dict, index):
    return list(dict.values())[index:]

def draw_graph(dic):
    long = dic.get('LON')
    lat = dic.get('LAT')
    Year = generate_sub_keylist(dic,2)
    Chloride_exposure_values = generate_sub_valuelist(dic, 2)
    Chloride_exposure_values = [ round(float(elem), 2) for elem in Chloride_exposure_values ]
    # print(keys, values)
    
    fig = go.Figure(data=go.Scatter(x=Year, y=Chloride_exposure_values))
    fig.update_layout(
    title=dict(
        text="Chloride exposure data on bridge corrosion at (" + lat[:5] + ", " + long[:5] + ")"

    ),
    xaxis_title=dict(text='Year'),
    yaxis_title=dict(text='Chloride exposure rate(kg/m^3)')
    )
    # plot_bgcolor='rgb(50, 50, 50)',
    # xaxis=dict(tickfont=dict(size=14, color='#FFFFFF')),
    # yaxis=dict(tickfont=dict(size=14, color='#FFFFFF')),
    # legend=dict(x=0.1, y=1.1, orientation='h', font=dict(color='#FFFFFF')),
    # margin=dict(l=10, r=10, t=100, b=50)

    div_string = plot(fig, output_type='div')
    # result = div_string
    return div_string


