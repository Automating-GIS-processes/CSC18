
.. figure:: img/Intro_PythonGIS_banner.png

Welcome to Introduction to Python GIS  -course 2018!
====================================================

**Introduction to Python GIS** is a 3-day course organized by `CSC Finland – IT Center for Science <https://www.csc.fi/>`__.
During the course you will learn how to do different GIS-related tasks in Python programming language.
Each lesson is a tutorial with specific topic(s) + Exercises where the aim is to learn
how to solve common GIS-related problems and tasks using Python tools.
The course is tailored to fit into three days based on materials from `Automating GIS processes <http://autogis.github.io>`__ -course
that is part of a GIS-track of the `Master's Program <https://www.helsinki.fi/en/programmes/master/geography>`__ at the Department of Geosciences and Geography, University of Helsinki.

Lecturer of the course is `Henrikki Tenkanen <https://www.researchgate.net/profile/Henrikki_Tenkanen>`__ who is a geo-data scientist and postdoctoral
researcher at the `Digital Geography Lab <http://helsinki.fi/digital-geography>`__, University of Helsinki.

In the lessons, we use only publicly available data which can be used and downloaded by anyone anywhere. In this course,
we assume that you know the basics of Python programming. If Python is not familiar to you, we recommend to start with a
course from us focusing on the basics of Python
from `geo-python.github.io <https://geo-python.github.io>`_.

Course format
-------------

The majority of this course will be spent in front of a computer learning to program in the Python language and working on exercises.
The provided exercises will focus on developing basic programming skills using the Python language and applying those skills to various GIS related problems.

Program
-------

The materials are divided into following themes:

+----------------+---------------------------------+
| Time           | Theme                           |
+================+=================================+
| **Lesson 1**   | GIS with Python;                |
|   Mon 9-12     | Spatial data model;             |
|                | Geometric Objects; Shapely      |
|                |                                 |
+----------------+---------------------------------+
|   *Mon 12-13*  |          *Lunch*                |
+----------------+---------------------------------+
| **Lesson 2**   | Working with GeoDataFrames;     |
|  Mon 13-16     | Managing projections;           |
|                |                                 |
+----------------+---------------------------------+
| **Lesson 3**   | Geocoding;                      |
|  Tue 9-12      | Table join;                     |
|                | Working with OpenStreetMap data |
|                |                                 |
+----------------+---------------------------------+
|   *Tue 12-13*  |          *Lunch*                |
+----------------+---------------------------------+
| **Lesson 4**   | Geometric operations;           |
|  Tue 13-16     | Spatial queries;                |
|                |                                 |
+----------------+---------------------------------+
| **Lesson 5**   | Visualization, making static    |
|  Wed 9-12      | and interactive maps            |
|                |                                 |
+----------------+---------------------------------+
|   *Wed 12-13*  |          *Lunch*                |
+----------------+---------------------------------+
| **Lesson 6**   | Raster processing in Python     |
|  Wed 13-16     |                                 |
+----------------+---------------------------------+

.. admonition:: Materials are available for you online, always!

    After finishing this course, you can always come back later to check the materials on this site, they will be available for you always.
    Materials are written in a way that you can follow them step by step exactly as they are written (requires only modifying the filepaths).

.. admonition:: More materials available!

   If you are eager to learn more, there are more materials available from `Automating GIS processes <http://autogis.github.io>`__ -course site, including:

     - `Python programming with QGIS 3.0 (processing -module) <https://automating-gis-processes.github.io/2017/lessons/L6/01-overview.html>`__
     - `Python programming with ArcGIS (arcpy -module) <https://automating-gis-processes.github.io/2016/Lesson6-overview.html>`__
     - `Network analysis in Python (with OSMnx + networkx -modules) <https://automating-gis-processes.github.io/2017/lessons/L7/network-analysis.html>`__
     - `Simplifying geometries in Python <https://automating-gis-processes.github.io/2017/lessons/L4/geometric-operations.html#simplifying-geometries>`__
     - `Aggregating (dissolving) geometries <https://automating-gis-processes.github.io/2017/lessons/L4/geometric-operations.html#aggregating-data>`__
     - `Interactive maps on Leaflet (folium module) <https://automating-gis-processes.github.io/2017/lessons/L5/interactive-map-folium.html>`__
     - `Raster processing with GDAL + interacting with GDAL from command line <https://automating-gis-processes.github.io/2016/Lesson7-overview.html>`__

Contents
--------
*Lesson content, readings and due dates are subject to change*

.. toctree::
   :maxdepth: 2
   :caption: Course information

   course-info/course-info
   course-info/who-are-you
   course-info/Installing_Anacondas_GIS
   course-info/License-terms

.. toctree::
   :maxdepth: 2
   :caption: Lesson 1

   lessons/L1/Intro-Python-GIS
   lessons/L1/overview
   lessons/L1/Geometric-Objects
   lessons/L1/ex-1
   lessons/L1/exercise-1-hints

.. toctree::
   :maxdepth: 2
   :caption: Lesson 2

   lessons/L2/overview
   lessons/L2/geopandas-basics
   lessons/L2/projections
   lessons/L2/using-functions
   lessons/L2/ex-2
   lessons/L2/exercise-2-hints

.. toctree::
   :maxdepth: 2
   :caption: Lesson 3

   lessons/L3/overview
   lessons/L3/geocoding
   lessons/L3/point-in-polygon
   lessons/L3/spatial-join
   lessons/L3/nearest-neighbour
   lessons/L3/ex-3
   lessons/L3/exercise-3-hints

.. toctree::
   :maxdepth: 2
   :caption: Lesson 4

   lessons/L4/overview
   lessons/L7/retrieve-osm-data
   lessons/L4/geometric-operations
   lessons/L4/ex-4
   lessons/L4/exercise-4-hints

.. toctree::
   :maxdepth: 2
   :caption: Lesson 5

   lessons/L5/overview
   lessons/L5/static-maps
   lessons/L5/interactive-map-bokeh
   lessons/L5/advanced-bokeh
   lessons/L5/share-on-github
   lessons/L5/ex-5
   lessons/L5/exercise-5-hints


.. toctree::
   :maxdepth: 2
   :caption: Lesson 6

   lessons/L7/overview
   lessons/L7/ex-7
   lessons/L7/exercise-7-hints
