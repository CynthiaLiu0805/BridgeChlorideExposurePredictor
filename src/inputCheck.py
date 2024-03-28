import geopandas as gpd
from numpy import shape
from shapely.geometry import Point
from flask import Flask, render_template, request

class InputCheck:
    def __init__(self, lon, lat):
        self.file_name = 'ontario_boundary.geojson'
        self.lon = lon
        self.lat = lat
        self.boundary = None
# Load the GeoJSON file of Canada provinces from a URL
# file_name = 'ontario_boundary.geojson'
    def load_file(self):
        try:
            self.boundary = gpd.read_file(self.file_name)
            # return boundary
        except FileNotFoundError as e:
            raise FileNotFoundError(f"FileNotFoundError: {e}")
        
    # def is_float(s):
    #     try:
    #         float(s)
    #         return True
    #     except ValueError as e:
    #         raise ValueError(f"InputTypeMismatchError: {e}")

    def convert_longitude(self):
        try:
            if (float(self.lon) > 0):
                return float(self.lon)-360
            return float(self.lon)
        except ValueError as e:
            raise ValueError(f"InputTypeMismatchError: {e}")

    def convert_latitude(self):
        try:
            return float(self.lat)
        except ValueError as e:
            raise ValueError(f"InputTypeMismatchError: {e}")

    
    # def convert_longitude(self, longitude):
    #     if (float(longitude) > 0):
    #         return float(longitude)-360
    #     return float(longitude)
    # def convert_latitude(self, latitude):
    #     return float(latitude)
        
    def is_within_ontario(self):
        try:
            # Generate from
            # https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/canada.geojson
            self.load_file()

            longitude = self.convert_longitude()
            latitude = self.convert_latitude()

            # Create a shapely Point object for the coordinate
            point = Point(longitude, latitude)

            # Iterate through each polygon in the boundary and check if the point is within it
            for polygon in self.boundary.geometry:
                # print(polygon)
                if polygon.contains(point):
                    return True
            return False 
        except Exception as e:
            raise e