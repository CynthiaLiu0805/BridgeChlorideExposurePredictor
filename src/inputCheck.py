import geopandas as gpd
from numpy import shape
from shapely.geometry import Point

# Load the GeoJSON file of Canada provinces from a URL
import requests
def is_within_ontario(latitude, longitude):
    # Load the GeoJSON file containing the boundary of Ontario
    try:
        # Generate from
        # https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/canada.geojson
        boundary = gpd.read_file('ontario_boundary.geojson')
        
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
        
    except Exception as e:
    
        print(f"Error: {e}")
        
    # If the point is not within any polygon, return False
        return False
      
