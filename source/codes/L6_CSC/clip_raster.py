# -*- coding: utf-8 -*-
"""
Clip Raster files.

Created on Sun Jan 14 12:39:54 2018

@author: Henrikki Tenkanen
"""

import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs

# Filepath
fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\Landsat\p188r018_7t20020529_z34__LV-FIN.tif"
out_tif = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\Landsat\Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"

def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

# Read the file with rasterio
data = rasterio.open(fp)

# Attributes of the raster file
# -----------------------------

width, height = data.width, data.height
crs = data.crs
band_cnt = data.count
name = data.name
bounds = data.bounds
driver = data.driver
nodata = data.nodatavals

# Plot the data (transform gives the etent labels)
#show(data)

# Plot the histogram
#show_hist(data)

# Clip the data based on Polygon

# Let's create a bounding box with Shapely
# WGS84 coordinates
minx, miny = 24.60, 60.00
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)

# Insert the bbox into a GeoDataFrame
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

# Re-project into the same coordinate system as the raster data
geo = geo.to_crs(crs=data.crs.data)
#shp_out = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\Landsat\Mask_polygon.shp"
#geo.to_file(shp_out)

# Get the geometry coordinates
coords = getFeatures(geo)

# Clip the raster with the polygon
out_img, out_transform = mask(raster=data, shapes=coords, crop=True)
# Copy the metadata
out_meta = data.meta.copy()

# Parse EPSG code
epsg_code = int(data.crs.data['init'][5:])

# Write the clipped raster to disk
out_meta.update({"driver": "GTiff",
                 "height": out_img.shape[1],
                 "width": out_img.shape[2],
                 "transform": out_transform,
                 "crs": pycrs.parser.from_epsg_code(epsg_code).to_proj4()}
                         )

with rasterio.open(out_tif, "w", **out_meta) as dest:
    dest.write(out_img)
    
clipped = rasterio.open(out_tif)
show((clipped, 5))    

# Show histogram for the clipped region
show_hist(clipped, bins=70, lw=0.0, stacked=False, alpha=0.3,
          histtype='stepfilled', title="Histogram")

