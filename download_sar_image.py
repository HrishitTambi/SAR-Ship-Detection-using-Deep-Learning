import os
import json
import sys
import ast
from shapely.geometry import shape
import urllib.request

def download_image(name, polygon):
    # Folder path containing the JSON files
    folder_path = os.path.join(os.getcwd(),  'items')

    # Define the polygon for filtering
    polygon = ast.literal_eval(polygon)
    poly = {
        "type": "Polygon",
        "coordinates": [polygon]
    }

    # Convert the polygon to a Shapely geometry
    polygon = shape(poly)
    results = []

    # Iterate through the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path) as file:
                data = json.load(file)

            # Access the 'geometry' attribute and perform intersection check
            if 'geometry' in data :
                geometry = data['geometry']
                if data['properties']['sar:product_type'] == "GEO":
                  geom = shape(geometry)
                  if geom.intersects(polygon):
                      results.append(data)

    # We download the first result
    url = results[0]['assets']["HH"]["href"]
    urllib.request.urlretrieve(url, name)
    print(f"Image downloaded successfully and saved as {name}")

name = sys.argv[1]
polygon = sys.argv[2]
download_image(name, polygon)
