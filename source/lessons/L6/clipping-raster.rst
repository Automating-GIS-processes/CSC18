Masking / clipping raster
=========================

One common task in raster processing is to clip raster files based on a Polygon.
The following example shows how to clip a large raster based on a bounding box around Helsinki Region.


.. ipython:: python

    import rasterio
    from rasterio.plot import show
    from rasterio.plot import show_hist
    from rasterio.mask import mask
    from shapely.geometry import box
    import geopandas as gpd
    from fiona.crs import from_epsg
    import pycrs

- Specify input and output filepaths

.. ipython:: pyhon

    # Filepaths
    fp = r"C:\HY-DATA\HENTENKA\CSC\Data\p188r018_7t20020529_z34__LV-FIN.tif"
    out_tif = r"C:\HY-DATA\HENTENKA\CSC\Data\Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"

- Open the raster in read mode

.. ipython:: python

    data = rasterio.open(fp)


- Plot the data

.. ipython:: python

    @savefig large_raster.png width=450px
    show(data)


- Next, we need to create a bounding box with Shapely

.. ipython:: python

    # WGS84 coordinates
    minx, miny = 24.60, 60.00
    maxx, maxy = 25.22, 60.35
    bbox = box(minx, miny, maxx, maxy)

- Insert the bbox into a GeoDataFrame

.. ipython:: python

    geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

-  Re-project into the same coordinate system as the raster data

.. ipython:: python

    geo = geo.to_crs(crs=data.crs.data)

- Next we need to get the coordinates of the geometry in such a format that rasterio wants them. This can be conducted easily with following function

.. code:: python

    def getFeatures(gdf):
        """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
        import json
        return [json.loads(gdf.to_json())['features'][0]['geometry']]


.. ipython:: python
   :suppress:

    def getFeatures(gdf):
        import json
        return [json.loads(gdf.to_json())['features'][0]['geometry']]

- Get the geometry coordinates by using the function.

.. ipython:: python

    coords = getFeatures(geo)
    print(coords)

Okey, so rasterio wants to have the coordinates of the Polygon in this kind of format.

- Now we are ready to clip the raster with the polygon using the ``coords`` variable that we just created. Clipping the raster
  can be done easily with the ``mask`` function that we imported in the beginning from ``rasterio``, and specifying ``clip=True``.

.. ipython:: python

    out_img, out_transform = mask(raster=data, shapes=coords, crop=True)

- Next, we need to modify the metadata. Let's start by copying the metadata from the original data file.

.. ipython:: python

    # Copy the metadata
    out_meta = data.meta.copy()
    print(out_meta)

- Next we need to parse the EPSG value from the CRS so that we can create a ``Proj4`` string using ``PyCRS`` library (to ensure that the projection information is saved correctly).

.. ipython:: python

    # Parse EPSG code
    epsg_code = int(data.crs.data['init'][5:])
    print(epsg_code)

- Now we need to update the metadata with new dimensions, transform (affine) and CRS (as Proj4 text)

.. ipython:: python

    out_meta.update({"driver": "GTiff",
                     "height": out_img.shape[1],
                     "width": out_img.shape[2],
                     "transform": out_transform,
                     "crs": pycrs.parser.from_epsg_code(epsg_code).to_proj4()}
                             )

- Finally, we can save the clipped raster to disk with following command.

.. ipython:: python

    with rasterio.open(out_tif, "w", **out_meta) as dest:
        dest.write(out_img)

- Let's still check that the result is correct by plotting our new clipped raster.

.. ipython:: python

    clipped = rasterio.open(out_tif)
    show((clipped, 5))

Great, it worked! This is how you can easily clip (*mask*) raster files with rasterio.


