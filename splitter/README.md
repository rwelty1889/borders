Splitter
========

Splitter is designed to follow ogr2osm in a work flow in order
to provide 2 functions. Please pardon my python, I'm still on the
learning curve.

1. simplified tag translations from shapefile attributes to OSM tags


2. directing entities (ways and relations) into different target files
depending on their tagging.

The intended use case is to use ogr2osm to extract data from, for
example, Census Bureau TIGER shapefiles, and then use splitter to
rewrite the tags and divide up the resulting entities. A good example
is the TIGER places shapefiles contain villages, cities and CDPs, which
we don't necessarily want to treat the same way in an OSM context.

Splitter is intentionally designed to drop in easily where ogr2osm is
already installed; it requires nothing additional, so if ogr2osm works,
then splitter will work.

TODO
----

1. improve on method for specifying tag rewrites, possibly moving to
a format similar to that of osmosis

2. create a similar format for describing splits of the data

3. Census Bureau LSAD tags are used inconsistently so there will need
to be some work on the destinationExample.py code
