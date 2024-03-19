import geopandas as gpd
from numpy import shape
from shapely.geometry import Point
from flask import Flask, render_template, request
# Load the GeoJSON file of Canada provinces from a URL

file_name = 'ontario_boundary.geojson'
def load_file(s):
    try:
        boundary = gpd.read_file(s)
        return boundary
    except FileNotFoundError as e:
        raise FileNotFoundError(f"FileNotFoundError: {e}")
    
def is_float(s):
    try:
        float(s)
        return True
    except ValueError as e:
        raise ValueError(f"InputTypeMismatchError: {e}")

def convert_longitude(longitude):
    if (float(longitude) > 0):
        return float(longitude)-360
    return float(longitude)
def convert_latitude(latitude):
    return float(latitude)
    
def is_within_ontario(latitude, longitude):
    # Load the GeoJSON file containing the boundary of Ontario
    try:
        # float(latitude)
        # float(longitude)
        
        # Generate from
        # https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/canada.geojson
        boundary = load_file(file_name)
        
        # If the longitude is positive, convert it to negative
        # if (float(longitude) > 0):
        #     longitude = float(longitude)-360

        longitude = convert_longitude(longitude)
        latitude = convert_latitude(latitude)

        # Create a shapely Point object for the coordinate
        point = Point(longitude, latitude)

        # Iterate through each polygon in the boundary and check if the point is within it
        for polygon in boundary.geometry:
            # print(polygon)
            if polygon.contains(point):
                return True
        return False 
    except Exception as e:
        raise e