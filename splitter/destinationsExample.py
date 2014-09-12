'''
example of setting up targets
'''

import tags
import destination

def setupTargets():
    t = [ destination.Target( "states.osm", [ tags.Tag( "place", "state")]), \
          destination.Target( "counties.osm", [ tags.Tag( "tiger:LSAD", "03"),
                                                tags.Tag( "tiger:LSAD", "04"),
                                                tags.Tag( "tiger:LSAD", "05"),
                                                tags.Tag( "tiger:LSAD", "06"),
                                                tags.Tag( "tiger:LSAD", "07"),
                                                tags.Tag( "tiger:LSAD", "10"),
                                                tags.Tag( "tiger:LSAD", "12"),
                                                tags.Tag( "tiger:LSAD", "13"),
                                                tags.Tag( "tiger:LSAD", "15"),
                                                tags.Tag( "tiger:LSAD", "25")
                                            ]), \
          destination.Target( "cdps.osm", [ tags.Tag( "place", "cdp")]), \
          destination.Target( "villages.osm", [ tags.Tag( "place", "village")]), \
          destination.Target( "citys.osm", [ tags.Tag( "place", "city")]), \
          destination.Target( "reservations.osm", [tags.Tag( "boundary", "aboriginal_lands")]), \
          destination.Target( "towns.osm", [tags.Tag( "place", "town")]), \
          destination.Target( "boroughs.osm", [tags.Tag( "place", "borough")])
          ]

    return t
