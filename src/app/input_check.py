'''
This module checks if the input from users is valid. 
If they are, the system will proceed to searching the input in database, 
else, it will produce warning message.
'''
import geopandas as gpd
from numpy import shape
from shapely.geometry import Point
from flask import Flask, render_template, request

class Input_check:
    def __init__(self, lon, lat):
        self.file_name = 'ontario_boundary.geojson' # Generate from https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/canada.geojson
 
        self.lon = lon
        self.lat = lat
        self.boundary = None

    # Load the GeoJSON file
    def load_file(self):
        try:
            self.boundary = gpd.read_file(self.file_name)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"FileNotFoundError: {e}")
        
    #  Convert the longitude to float, and make it negative because the record in geojson file is negative
    def convert_longitude(self):
        try:
            if (float(self.lon) > 0):
                return float(self.lon)-360
            return float(self.lon)
        except ValueError as e:
            raise ValueError(f"InputTypeMismatchError: {e}")

    # Convert the latitude to float
    def convert_latitude(self):
        try:
            return float(self.lat)
        except ValueError as e:
            raise ValueError(f"InputTypeMismatchError: {e}")

    # Check if the input is inside Ontario
    def is_within_ontario(self):
        try:
            self.load_file()

            longitude = self.convert_longitude()
            latitude = self.convert_latitude()

            # Create a shapely Point object for the coordinate
            point = Point(longitude, latitude)

            # Iterate through each polygon in the boundary and check if the point is within it
            for polygon in self.boundary.geometry:
                if polygon.contains(point):
                    return True
            return False 
        except Exception as e:
            raise e