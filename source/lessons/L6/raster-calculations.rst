Raster calculations
===================

Conducting calculations between bands or raster is another common GIS task. Here, we will be calculating ``NDVI`` (Normalized difference vegetation index)
based on the Landsat dataset that we have downloaded from Helsinki region. Conducting calculations with rasterio
is fairly straightforward if the extent etc. matches because the values of the rasters are stored as ``numpy`` arrays
(similar to the columns stored in Geo/Pandas, i.e. ``Series``).

- Let's start by importing the necessary modules ``rasterio`` and ``numpy``

.. ipython:: python

    import rasterio
    import numpy as np
    from rasterio.plot import show

- Let's read the file that we masked for Helsinki Region

.. ipython:: python

    # Filepath
    fp = r"C:\HY-DATA\HENTENKA\CSC\Data\Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"
    raster = rasterio.open(fp)

For calculating the NDVI (Normalized difference vegetation index) you need two bands: band-4 which is the Red channel and band-5 which is the Near Infrared (NIR)

- Let's read those bands from our raster source

.. ipython:: python

    red = raster.read(4)
    nir = raster.read(5)
    red
    nir
    type(nir)
    @savefig nir_channel.png width=450px
    show(nir)

As we can see the values are stored as numpy.ndarray.

- Let's change the data type from uint8 to float so that we can have floating point numbers stored in our arrays.

.. ipython:: python

    red = red.astype(float)
    nir = nir.astype(float)
    nir

Now we can see that the numbers changed to decimal numbers (there is a dot after the zero).

Next we need to tweak the behaviour of numpy a little bit. By default numpy will complain about dividing with zero values.
We need to change that behaviour because we have a lot of 0 values in our data.

- Allow 0 division in numpy

.. ipython:: python

    np.seterr(divide='ignore', invalid='ignore')

Now we need to initialize the ndvi with zeros before we do the calculations (this is numpy specific trick)

.. ipython:: python

    ndvi = np.empty(raster.shape, dtype=rasterio.float32)

- Now we are ready to calculate the NDVI. First, we can create a filter where we calculate the values on such pixels that have a value larger than 0.

.. ipython:: python

    check = np.logical_or ( red > 0, nir > 0 )

- Now we can apply that filter and calculate the ndvi index.

.. ipython:: python

    ndvi = np.where ( check,  (nir - red ) / ( nir + red ), -999 )
    ndvi
    ndvi.mean()
    ndvi.std()
    @savefig ndvi.png width=450px
    show(ndvi, cmap='summer')


