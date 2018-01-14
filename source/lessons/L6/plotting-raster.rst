Visualizing raster
==================

Of course, it is always highly useful to take a look how the data looks like. This is easy with the ``rasterio.plot.show()`` function of rasterio.

.. ipython:: python

    import rasterio
    from rasterio.plot import show

    fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\Landsat\Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"

    # Open the file:
    raster = rasterio.open(fp)

    @savefig raster_image.png width=600px
    show(raster)

You can also plot different individual channels.

.. ipython:: python

    @savefig raster_image.png width=400px align=left
    show(raster)

Histogram of the values
=======================

Quite often it is useful to