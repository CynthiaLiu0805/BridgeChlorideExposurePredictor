import geopandas as gpd
from numpy import shape
from shapely.geometry import Point
from flask import Flask, render_template, request
# Load the GeoJSON file of Canada provinces from a URL

def load_file(s):
    try:
        boundary = gpd.read_file(s)
        return boundary
    except FileNotFoundError as e:
        raise FileNotFoundError(f"FileNotFoundError: {e}")
    
def is_within_ontario(latitude, longitude):
    # Load the GeoJSON file containing the boundary of Ontario
    try:
        float(latitude)
        float(longitude)
        
        # Generate from
        # https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/canada.geojson
        boundary = load_file('ontario_boundary.geojson')
        # boundary = gpd.read_file('https://github.com/CynthiaLiu0805/BridgeCorrosion/blob/main/src/ontario_boundary.geojson')
        
        # If the longitude is positive, convert it to negative
        if (float(longitude) > 0):
            longitude = float(longitude)-360

        # Create a shapely Point object for the coordinate
        point = Point(longitude, latitude)

        # Iterate through each polygon in the boundary and check if the point is within it
        for polygon in boundary.geometry:
            # print(polygon)
            if polygon.contains(point):
                return True
        return False 
    except ValueError as e:
        raise ValueError(f"InputTypeMismatchError: {e}")
    
print(is_within_ontario(44.550356, -80.84538))