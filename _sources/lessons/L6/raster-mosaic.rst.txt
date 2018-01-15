Creating a raster mosaic
========================

Quite often you need to merge multiple raster files together and create a *raster mosaic*. This can be done
easily with the ``merge()`` function in Rasterio.

Here, we will create a mosaic based on 2X2m resolution DEM files (altogether 12 files) covering the Helsinki Metropolitan region. If you have not downloaded the DEM files
yet, you can do that by running the script from :doc:`download-data` section.

- Let's start by importing required modules and functions.

.. ipython:: python

    import rasterio
    from rasterio.merge import merge
    from rasterio.plot import show
    import glob
    import os

As there are many ``tif`` files in our folder, it is not really pracical to start listing them manually. Luckily,
we have a module and function called ``glob`` that can be used to create a list of those files that we are interested
in based on search criteria.

- Find all ``tif`` files from the folder where the file starts with ``L`` -letter.

.. ipython:: python

    # File and folder paths
    dirpath = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\CSC_Lesson6"
    out_fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\Data\CSC_Lesson6\Helsinki_DEM_2x2m_Mosaic.tif"

    # Make a search criteria to select the DEM files
    search_criteria = "L*.tif"
    q = os.path.join(dirpath, search_criteria)
    print(q)

Now we can see that we have a search criteria (``q``) that we can pass to ``glob`` function.

- List all dem files with glob() function

.. ipython:: python

    dem_fps = glob.glob(q)
    dem_fps

Great! Now we have all those 12 files in a list and we can start to make a mosaic out of them.


- Let's first create an empty list for the datafiles that will be part of the mosaic.

.. ipython:: python

    src_files_to_mosaic = []

- Now we open all those files in read mode with raterio and add those files into a our source file list.

.. ipython:: python

    for fp in dem_fps:
        src = rasterio.open(fp)
        src_files_to_mosaic.append(src)

    src_files_to_mosaic

Okey, now we can see that we have a list full of open raster objects.

- Now it is really easy to merge those together and create a mosaic with rasterio's ``merge`` function.

.. ipython:: python

    # Merge function returns a single mosaic array and the transformation info
    mosaic, out_trans = merge(src_files_to_mosaic)

- Let's check that it looks okey.

.. ipython:: python

    @savefig raster_mosaic.png width=400px
    show(mosaic, cmap='terrain')

Great, it looks correct! Now we are ready to save our mosaic to disk.

- Let's first update the metadata with our new dimensions, transform and CRS

.. ipython:: python

    # Copy the metadata
    out_meta = src.meta.copy()

    # Update the metadata
    out_meta.update({"driver": "GTiff",
                     "height": mosaic.shape[1],
                     "width": mosaic.shape[2],
                     "transform": out_trans,
                     "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                     }
                    )

- Finally we can write our mosaic to our computer

.. ipython:: python

    # Write the mosaic raster to disk
    with rasterio.open(out_fp, "w", **out_meta) as dest:
        dest.write(mosaic)

That's it! Easy!