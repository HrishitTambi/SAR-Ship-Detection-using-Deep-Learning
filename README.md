# SAR-Ship-Detection-using-Deep-Learning
## How to run the code

### Requirements

- **Python 3.9**+
- For optimal performance, it is recommended to run the program in Google Colab due to its availability of high computational resources and ample memory.
### Installing Dependencies

1. You can run the command given below in Google Colab to install all neccessary libraries.

```shell
!pip install gdal numpy pandas shapely matplotlib pytorch torchvision rasterio ipython tqdm geopandas geojson
```
## To Run

1) Clone this repository.
2) Download a Capella SAR image where you can perform ship detection. You can download a Capella image which intersect with a certain polygon using the below command:
```shell
python download_sar_image.py output_tif_filename intersecting_polygon_coordinates
```
   Example: 
```shell
python download_sar_image.py new_img.tif "[[112.65398084, -7.17831176], [112.68703848, -7.14747203], [112.75027304, -7.21506447], [112.71688043, -7.24622707], [112.65398084, -7.17831176]]"
```
3) Convert the CRS of the .tif image to EPSG:4326 (Can be performed in QGIS).
4) Run: 
```shell
python SAR.py input_tif_name output_geojson_filename prediction_confidence_threshold 
```
   Example: 
```shell
python SAR.py input_img.tif detections.geojson 0.5
```
5) Plot detections / imagery in GIS software. Use the "onshore_detection" field in the output geojson file to filter out erronous detections on land. Alternatively, use the "detection_confidence" field to visualise the model's confidence that a given detection is a ship. 

### Data Specifics
The datatype of the tile should be an `8-bit` integer.
