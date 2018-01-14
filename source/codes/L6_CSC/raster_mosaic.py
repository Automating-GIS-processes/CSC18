# -*- coding: utf-8 -*-
"""
Merge rasters together

Created on Sun Jan 14 21:46:54 2018

@author: Henrikki Tenkanen
"""

import rasterio
import numpy as np
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os

# Find all ``tif`` files from the folder where the file starts with ``L`` -letter.
dirpath = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\CSC_Lesson6"
out_fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\CSC_Lesson6\Helsinki_DEM_2x2m_Mosaic.tif"

# Make a search criteria to select the DEM files
search_criteria = "L*.tif"
q = os.path.join(dirpath, search_criteria)

# List all dem files with glob() function
dem_fps = glob.glob(q)

# Create a list for the files that will be part of the mosaic
src_files_to_mosaic = []

# Open the files in read mode with raterio and add those files into a list
for fp in dem_fps:
    src = rasterio.open(fp)
    print(src.crs)
    src_files_to_mosaic.append(src)

# The merge function returns a single array and the affine transform info
mosaic, out_trans = merge(src_files_to_mosaic)

# Check to make sure the merge looks good.
#show(mosaic)

# Copy the metadata
out_meta = src.meta.copy()

# Update the metadata with correct width and height, transform and CRS
out_meta.update({"driver": "GTiff",
                 "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                 "transform": out_trans,
                 "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                 }
                ) 
# Write the mosaic raster to disk
with rasterio.open(out_fp, "w", **out_meta) as dest:
    dest.write(mosaic)