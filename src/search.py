import numpy as np
from flask import Flask, render_template, request
import pandas as pd
from visualization import Visualization

data_name ='results.csv'

class Search:

    def __init__(self, lon, lat):
        self.file_name = 'results.csv'
        self.lon = lon
        self.lat = lat
        self.data = None

    # fig = go.Figure()
    def load_data(self):
        # Load CSV data
        try:
            self.data = pd.read_csv(self.file_name)
            # return data
        except FileNotFoundError:
            raise FileNotFoundError("The file is not found. Please make sure the file is in the same directory as the app.py file.")

    def find_closest(self):
        lon_calculate =float(self.lon)
        if (float(self.lon) < 0):
            lon_calculate = float(self.lon)+360
        # Calculate the Euclidean distance for each row
        distances = np.sqrt((self.data['LAT'] - float(self.lat))**2 + (self.data['LON'] - float(lon_calculate))**2)
        # print(data['LAT'])
        # print(distances)
        
        # Get the index of the smallest distance
        closest_index = distances.idxmin()
        # print("cloest",distances.min(), closest_index)
        # Return the row with the smallest distance
        return self.data.loc[closest_index]


    # def convert_lon_calculate(self):
    #     lon_calculate =float(self.lon)
    #     if (float(self.lon) < 0):
    #         lon_calculate = float(self.lon)+360
    #     return lon_calculate

    def search_coordinates(self):
        result = None
        # lat = handleData.lat
        # lon = handleData.lon
        # Get coordinates from form or map click
        # lat = float(request.form['latitude'])
        # lon = float(request.form['longitude'])
        # print(lat, lon)
        # if (type(lat) == str):
        #     lon_calculate = float(lon)

        # lon_calculate =lon
        # if (lon < 0):
        #     lon_calculate = lon+360
        # lon_calculate = self.convert_lon_calculate()


        # Load CSV data
        self.load_data()
        # print(self.data)

        # Find the closest row
        result = self.find_closest()
        # print(result)

        # Convert the result to a dictionary to be able to pass it to the template
        result_dict = result.to_dict()
        # update result dict according to the input
        result_dict['LAT'] = str(self.lat)
        result_dict['LON'] = str(self.lon)

        visual = Visualization(result_dict)
        visual.draw_grpah()

        return render_template('index.html', result=result_dict, div_string=visual.result)
        