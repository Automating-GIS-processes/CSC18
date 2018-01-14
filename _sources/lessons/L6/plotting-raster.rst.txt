Visualizing raster layers
=========================

Of course, it is always highly useful to take a look how the data looks like. This is easy with the ``rasterio.plot.show()`` function of rasterio.

Basic plotting
--------------

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

    @savefig raster_band_red.png width=220px align=left
    show((raster, 4), cmap='Reds')

    @savefig raster_band_green.png width=220px align=left
    show((raster, 3), cmap='Greens')

    @savefig raster_band_blue.png width=220px align=left
    show((raster, 1), cmap='Blues')

Histogram of the raster data
----------------------------

It is fairly common that you want to look at the histogram of your data.
Luckily that is really easy to do with rasterio by using the ``rasterio.plot.show_hist()`` function.

- Let's draw the histogram of our raster dataset

.. ipython:: python

    from rasterio.plot import show_hist
    @savefig raster_histogram.png width=500px
    show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3,
          histtype='stepfilled', title="Histogram")

False color composite
---------------------

.. todo::

    Add materials about how to stack bands and create a false color composite.