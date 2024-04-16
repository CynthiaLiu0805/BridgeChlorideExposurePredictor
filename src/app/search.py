"""
This module searchs the input in the database
"""
import numpy as np
from flask import render_template
import pandas as pd
import visualization 

class Search:

    def __init__(self, lon, lat):
        self.file_name = 'results.csv'
        self.lon = lon
        self.lat = lat
        self.data = None

    # Load the database file
    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_name)
        except FileNotFoundError:
            raise FileNotFoundError("The file is not found. Please make sure the file is in the same directory as the app.py file.")

    # Find the closest point in the database
    def find_closest(self):
        lon_calculate =float(self.lon)
        if (float(self.lon) < 0):
            lon_calculate = float(self.lon)+360
        # Calculate the Euclidean distance for each row
        distances = np.sqrt((self.data['LAT'] - float(self.lat))**2 + (self.data['LON'] - float(lon_calculate))**2)
        # Get and return the index of the smallest distance
        closest_index = distances.idxmin()
        return closest_index


    def search_coordinates(self):
        result = None
        # Load database
        self.load_data()
        # Find the closest row
        closest_index = self.find_closest()
        result = self.data.loc[closest_index]
        # Convert the result to a dictionary to be able to pass it to the template
        result_dict = result.to_dict()
        # Update result dict to match the input, cast it to two decimal for readability
        result_dict['LAT'] = str(self.lat[:5])
        result_dict['LON'] = str(self.lon[:5])
        result = visualization.draw_graph(result_dict)
        return render_template('index.html', result=result_dict, div_string=result)
        