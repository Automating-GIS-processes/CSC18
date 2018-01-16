# -*- coding: utf-8 -*-
"""
Raster calculations. NDVI

Created on Tue Jan 16 21:29:26 2018

@author: Henrikki Tenkanen
"""
import rasterio
import numpy as np
from rasterio.plot import show

# Filepath
fp = r"C:\HY-DATA\HENTENKA\CSC\Data\Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"
fp = r"C:\HY-DATA\HENTENKA\CSC\Data\RGB.byte.tif"


# Lets' start by opening the data
raster = rasterio.open(fp)

# For calculating the NDVI (Normalized difference vegetation index) you need two bands: band-4 which is the Red channel and band-5 which is the Near Infrared (NIR)

# Let's read those bands from our raster source
red = raster.read(4)
nir = raster.read(5)
red
nir
type(nir)
show(red)

# As we can see the values are stored as numpy.ndarray. Let's change the data type from uint8 to float so that we can have floating point numbers stored in our arrays.
red = red.astype(float)
nir = nir.astype(float)
nir

# Now we can see that the numbers changed to decimal numbers (there is a dot after the zero).

# Next we need to tweak the behaviour of numpy a little bit. By default numpy will complain about dividing with zero values. 
# We need to change that behaviour because we have a lot of 0 values in our data. 

# - Allow 0 division in numpy

np.seterr(divide='ignore', invalid='ignore')

# Now we need to initialize the ndvi with zeros before we do the calculations (this is numpy specific trick)
ndvi = np.empty(raster.shape, dtype=rasterio.float32)

# - Now we are ready to calculate the NDVI. It is extremely easy with numpy arrays and can be performed as follows:
check = np.logical_or ( red > 0, nir > 0 )

ndvi = np.where ( check,  (nir - red ) / ( nir + red ), -999 ) 
show(ndvi, cmap='summer')    


