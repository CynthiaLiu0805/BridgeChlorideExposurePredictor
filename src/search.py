import numpy as np
from flask import Flask, render_template, request
import pandas as pd
import matplotlib
import visualization

# fig = go.Figure()
def load_data():
    # Load CSV data
    data = pd.read_csv('data.csv')
    return data

def find_closest(lat, lon, data):
    # Calculate the Euclidean distance for each row
    distances = np.sqrt((data['LAT'] - float(lat))**2 + (data['LON'] - float(lon))**2)
    # print(data['LAT'])
    # print(distances)
    
    # Get the index of the smallest distance
    closest_index = distances.idxmin()
    # print("cloest",distances.min(), closest_index)
    # Return the row with the smallest distance
    return data.loc[closest_index]


def search_coordinates():
    result = None
    # Get coordinates from form or map click
    lat = request.form['latitude']
    lon = request.form['longitude']
    # print(lat, lon)
    if (type(lat) == str):
        lon_calculate = float(lon)
    if (lon_calculate < 0):
            lon_calculate = lon_calculate+360


    # Load CSV data
    data = load_data()

    # Find the closest row
    result = find_closest(lat, lon_calculate, data)
    # print(result)

    # Convert the result to a dictionary to be able to pass it to the template
    result_dict = result.to_dict()
    # update result dict according to the input
    result_dict['LAT'] = str(lat)
    result_dict['LON'] = str(lon)

    div_string = visualization.draw_grpah(result_dict)

    return render_template('index.html', result=result_dict, div_string=div_string)
    