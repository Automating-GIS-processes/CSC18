Raster calculations
===================

Conducting calculations between bands or raster is another common GIS task. Here, we will be calculating ``NDVI``
based on the Landsat dataset that we have downloaded from Helsinki region. Conducting calculations with rasterio
is fairly straightforward if the extent etc. matches because the values of the rasters are stored as ``numpy`` arrays
(similar to the columns stored in Geo/Pandas, i.e. ``Series``).

