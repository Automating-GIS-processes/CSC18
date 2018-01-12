Geometric operations
====================

Overlay analysis
----------------

The aim here is to make an overlay analysis where we clip polygon data
based on the borders of municipality of Helsinki.

Let's first read the data.

.. code:: python

    import geopandas as gpd
    import matplotlib.pyplot as plt
    import shapely.speedups

    # Let's enable speedups to make queries faster
    shapely.speedups.enable()

    # File paths
    border_fp = "/home/geo/data/Helsinki_borders.shp"
    poly_fp = "/home/geo/data/TravelTimes_to_5975375_RailwayStation.shp"

    # Read files
    poly = gpd.read_file(grid_fp)
    hel = gpd.read_file(border_fp)

.. ipython:: python
   :suppress:

    import gdal
    import geopandas as gpd
    import os
    import matplotlib.pyplot as plt
    import shapely.speedups
    shapely.speedups.enable()
    border_fp = os.path.join(os.path.abspath('data'), "Helsinki_borders.shp")
    poly_fp = os.path.join(os.path.abspath('data'), "Corine2012_Uusimaa.shp")
    poly = gpd.read_file(poly_fp)
    hel = gpd.read_file(border_fp)

Let's check that the coordinate systems match.

.. ipython:: python

    hel.crs
    poly.crs

Indeed, they do. This is pre-requisite to conduct spatial operations between the layers (as their coordinates need to match).

Let's see how our datasets look like. We will use the Helsinki municipality layer as our basemap and
plot the other layer on top of that.

.. ipython:: python


    basemap = hel.plot()
    poly.plot(ax=basemap, facecolor='gray' linewidth=0.02);

    # Use tight layout
    @savefig helsinki_poly_borders.png width=7in
    plt.tight_layout()

Let's do an overlay analysis and select polygons from landuse data that intersect with our Helsinki layer.

.. note::

   This can be a slow procedure with less powerful computer. There is a way to
   overcome this issue by doing the analysis **in batches** which is explained below, see the performance-tip_.

.. ipython:: python

    result = gpd.overlay(poly, hel, how='intersection')

Let's plot our data and see what we have.

.. ipython:: python

    result.plot(color="b")
    @savefig helsinki_poly_borders_intersect.png width=7in
    plt.tight_layout()

Cool! Now as a result we have only those polygons included that intersect with the Helsinki borders.
Notice that the polygons are clipped based on the boundary of the Helsinki borders.

Whatabout the data attributes? Let's see what we have.

.. ipython:: python

    result.head()

Nice! Now we have attributes from both layers included.

Let's see the length of the GeoDataFrame.

.. ipython:: python

    len(result)

And the original data.

.. ipython:: python

    len(poly)

Let's save our result poly as a GeoJSON file that is another commonly used file
format nowadays for storing spatial data.

.. code:: python

    resultfp = "/home/geo/data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

    # Use GeoJSON driver
    result.to_file(resultfp, driver="GeoJSON")

.. ipython:: python
   :suppress:

    resultfp = os.path.join(os.path.abspath('data'), "TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
    result.to_file(resultfp, driver="GeoJSON")

There are many more examples for different types of overlay analysis in `Geopandas documentation  <http://geopandas.org/set_operations.html>`_ where you can go and learn more.

