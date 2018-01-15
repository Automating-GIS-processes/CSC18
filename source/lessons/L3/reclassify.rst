Data reclassification
=====================

Reclassifying data based on specific criteria is a common task when doing GIS analysis.
The purpose of this lesson is to see how we can reclassify values based on some criteria which can be whatever, such as:

.. code::

    1. if travel time to my work is less than 30 minutes

    AND

    2. the rent of the apartment is less than 1000 € per month

    ------------------------------------------------------

    IF TRUE: ==> I go to view it and try to rent the apartment
    IF NOT TRUE: ==> I continue looking for something else

In this tutorial, we will use Travel Time Matrix data from Helsinki to
classify some features of the data based on map classifiers that are commonly used e.g. when doing visualizations,
and our own self-made classifier where we determine how the data should be classified.

1. use ready made classifiers from pysal -module to classify travel times into multiple classes.

2. use travel times and distances to find out

   - good locations to buy an apartment with good public transport accessibility to city center
   - but from a bit further away from city center where the prices are presumably lower.

Download data
-------------

Download (and then extract) the dataset zip-package used during this lesson `from this link <https://github.com/Automating-GIS-processes/Lesson-4-Classification-overlay/raw/master/data/data.zip>`_.

You should have following Shapefiles in the ``data`` folder:

.. code:: bash

   $ cd /home/geo/L4/data
   $ ls
   Corine2012_Uusimaa.cpg      Helsinki_borders.cpg                       TravelTimes_to_5975375_RailwayStation.dbf
   Corine2012_Uusimaa.dbf      Helsinki_borders.dbf                       TravelTimes_to_5975375_RailwayStation.prj
   Corine2012_Uusimaa.prj      Helsinki_borders.prj                       TravelTimes_to_5975375_RailwayStation.shp
   Corine2012_Uusimaa.shp      Helsinki_borders.shp                       TravelTimes_to_5975375_RailwayStation.shx
   Corine2012_Uusimaa.shp.xml  Helsinki_borders.shx
   Corine2012_Uusimaa.shx      TravelTimes_to_5975375_RailwayStation.cpg

*Note, during this intensive course we won't be using the Corine2012 data.*

Classifying data
----------------

Classification based on common classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Pysal <http://pysal.readthedocs.io/en/latest/>`_ -module is an extensive Python library including various functions and tools to
do spatial data analysis. It also includes all of the most common data classifiers that are used commonly e.g. when visualizing data.
Available map classifiers in pysal -module are (`see here for more details <http://pysal.readthedocs.io/en/latest/library/esda/mapclassify.html>`_):

 - Box_Plot
 - Equal_Interval
 - Fisher_Jenks
 - Fisher_Jenks_Sampled
 - HeadTail_Breaks
 - Jenks_Caspall
 - Jenks_Caspall_Forced
 - Jenks_Caspall_Sampled
 - Max_P_Classifier
 - Maximum_Breaks
 - Natural_Breaks
 - Quantiles
 - Percentiles
 - Std_Mean
 - User_Defined

First, we need to read our Travel Time data from Helsinki into memory from the GeoJSON file that `we prepared earlier <Lesson4-geometric-operations.html>`_ with overlay analysis.

.. code:: python

   fp = r"/home/geo/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

   # Read the GeoJSON file similarly as Shapefile
   acc = gpd.read_file(fp)

   # Let's see what we have
   acc.head(2)

.. ipython:: python
   :suppress:

     import gdal
     import geopandas as gpd
     import os
     fp = os.path.join(os.path.abspath('data'), "TravelTimes_to_5975375_RailwayStation_Helsinki.geojson")
     acc = gpd.read_file(fp)
     acc.head(2)

Okey we have plenty of different variables (see `from here the description <http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/>`_
for all attributes) but what we are
interested in are columns called ``pt_r_tt`` which is telling the time in minutes that it takes to reach city center
from different parts of the city, and ``walk_d`` that tells the network distance by roads to reach city center
from different parts of the city (almost equal to Euclidian distance).

**The NoData values are presented with value -1**. Thus we need to remove those first.

.. ipython:: python

   acc = acc.ix[acc['pt_r_tt'] >=0]

Let's plot it and see how our data looks like.

.. ipython:: python

   import matplotlib.pyplot as plt

   # Plot using 9 classes and classify the values using "Fisher Jenks" classification
   acc.plot(column="pt_r_tt", scheme="Fisher_Jenks", k=9, cmap="RdYlBu", linewidth=0);

   # Use tight layour
   @savefig pt_time.png width=7in
   plt.tight_layout()

Okey so from this figure we can see that the travel times are lower in the south where
the city center is located but there are some areas of "good" accessibility also in some other areas
(where the color is red).

Let's also make a plot about walking distances

.. ipython:: python

   acc.plot(column="walk_d", scheme="Fisher_Jenks", k=9, cmap="RdYlBu", linewidth=0);

   # Use tight layour
   @savefig walk_distances.png width=7in
   plt.tight_layout();

Okey, from here we can see that the walking distances (along road network) reminds
more or less Euclidian distances.

Let's apply one of those classifiers into our data and classify the travel times by public transport into 9 classes.

.. ipython:: python

  import pysal as ps

  # Define the number of classes
  n_classes = 9

The classifier needs to be initialized first with ``make()`` function that takes the number of desired classes as input parameter.

.. ipython:: python

  # Create a Natural Breaks classifier
  classifier = ps.Natural_Breaks.make(k=n_classes)

Now we can apply that classifier into our data quite similarly as in our previous examples.

.. ipython:: python

  # Classify the data
  classifications = acc[['pt_r_tt']].apply(classifier)

  # Let's see what we have
  classifications.head()

Okey, so we have a DataFrame where our input column was classified into 9 different classes (numbers 1-9) based on `Natural Breaks classification <http://wiki-1-1930356585.us-east-1.elb.amazonaws.com/wiki/index.php/Jenks_Natural_Breaks_Classification>`_.

Now we want to join that reclassification into our original data but let's first rename the column so that we recognize it later on.

.. ipython:: python

  # Rename the column so that we know that it was classified with natural breaks
  classifications.columns = ['nb_pt_r_tt']

  # Join with our original data (here index is the key
  acc = acc.join(classifications)

  # Let's see how our data looks like
  acc.head()

Great, now we have those values in our accessibility GeoDataFrame. Let's visualize the results and see how they look.

.. ipython:: python

    # Plot
    acc.plot(column="nb_pt_r_tt", linewidth=0, legend=True);

    # Use tight layour
    @savefig natural_breaks_pt_accessibility.png width=7in
    plt.tight_layout()

And here we go, now we have a map where we have used one of the common classifiers to classify our data into 9 classes.

Creating a custom classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multicriteria data classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's create a function where we classify the geometries into two classes based on a given ``threshold`` -parameter.
If the area of a polygon is lower than the threshold value (average size of the lake), the output column will get a value 0,
if it is larger, it will get a value 1. This kind of classification is often called a `binary classification <https://en.wikipedia.org/wiki/Binary_classification>`_.


First we need to create a function for our classification task. This function takes a single row of the GeoDataFrame as input,
plus few other parameters that we can use.

It also possible to do classifiers with multiple criteria easily in Pandas/Geopandas by extending the example that we started earlier.
Now we will modify our binaryClassifier function a bit so that it classifies the data based on two columns.

Let's call it customClassifier2 as it takes into account two criteria:

.. code:: python

   def customClassifier2(row, src_col1, src_col2, threshold1, threshold2, output_col):
       # 1. If the value in src_col1 is LOWER than the threshold1 value
       # 2. AND the value in src_col2 is HIGHER than the threshold2 value, give value 1, otherwise give 0
       if row[src_col1] < threshold1 and row[src_col2] > threshold2:
           # Update the output column with value 0
           row[output_col] = 1
       # If area of input geometry is higher than the threshold value update with value 1
       else:
           row[output_col] = 0

       # Return the updated row
       return row

.. ipython:: python
  :suppress:

    def customClassifier2(row, src_col1, src_col2, threshold1, threshold2, output_col):
        if row[src_col1] < threshold1 and row[src_col2] > threshold2:
            row[output_col] = 1
        else:
            row[output_col] = 0
        return row

Okey, now we have our classifier ready, let's use it to our data.

Let's do our classification based on two criteria
and find out grid cells where the **travel time is lower or equal to 20 minutes** but they are further away
**than 4 km (4000 meters) from city center**.

Let's create an empty column for our classification results called "Suitable_area".

.. ipython:: python

   acc["Suitable_area"] = None

Now we are ready to apply our custom classifier to our data with our own criteria.

.. ipython:: python

   acc = acc.apply(customClassifier2, src_col1='pt_r_tt', src_col2='walk_d', threshold1=20, threshold2=4000, output_col="Suitable_area", axis=1)

Let's see what we got.

.. ipython:: python

   acc.head()

Okey we have new values in ``Suitable_area`` .column.

How many Polygons are suitable for us? Let's find out by using a Pandas function called ``value_counts()`` that return the count of
different values in our column.

.. ipython:: python

   acc['Suitable_area'].value_counts()

Okey so there seems to be nine suitable locations for us where we can try to find an appartment to buy
Let's see where they are located.

.. ipython:: python

   # Plot
   acc.plot(column="Suitable_area", linewidth=0);

   # Use tight layour
   @savefig suitable_areas.png width=7in
   plt.tight_layout();

A-haa, okey so we can see that suitable places for us with our criteria seem to be located in the
eastern part from the city center. Actually, those locations are along the metro line which makes them
good locations in terms of travel time to city center since metro is really fast travel mode.

