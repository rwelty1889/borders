'''
example of setting up targets
'''

import tags
import destination

def setupTargets():
    t = [ destination.Target( "states.osm", [ tags.Tag( "place", "state")]), \
          destination.Target( "cdps.osm", [ tags.Tag( "place", "cdp")]), \
          destination.Target( "villages.osm", [ tags.Tag( "place", "village")]), \
          destination.Target( "citys.osm", [ tags.Tag( "place", "city")]), \
          destination.Target( "reservations.osm", [tags.Tag( "boundary", "aboriginal_lands")]), \
          destination.Target( "towns.osm", [tags.Tag( "place", "town")]), \
          destination.Target( "boroughs.osm", [tags.Tag( "place", "borough")])
          ]

    return t
