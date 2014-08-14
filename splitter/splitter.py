#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' splitter

This program performs two functions: it splits a .osm format file of
boundaries into subfiles based on boundary types, and it also converts tiger
tags into osm equivalents on the fly. how the split is done and what tags
are converted are controlled by an xml configuration file.

'''

import optparse
import logging as log
log.basicConfig( level=log.DEBUG, format="%(message)s")

import tags
import tagsExample
import destination
import destinationsExample

try:
    from lxml import etree
    log.debug("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.ElementTree as etree
        log.debug("running with ElementTree on Python 2.5+")
    except ImportError:
        try:
            # normal cElementTree install
            import cElementTree as etree
            log.debug("running with cElementTree")
        except ImportError:
            try:
                # normal ElementTree install
                import elementtree.ElementTree as etree
                log.debug("running with ElementTree")
            except ImportError:
                log.error("Failed to import ElementTree from any known place")
                raise


usage = "usage: %prog SRCFILE"
parser = optparse.OptionParser(usage=usage)

# Parse and process arguments
(options, args) = parser.parse_args()

sourceFile = args[0]

# all tag translations
translations = tagsExample.setupTranslations()

# all destination
destinations = destinationsExample.setupTargets()

sourceStream = open( sourceFile, "rb")

root = etree.parse( sourceFile).getroot()

children = list( root)

# iterate over all elements, process as appropriate

for child in children:
    if child.tag == 'node' :
        destination.allNodes[child.get( "id")] = child
    elif child.tag == 'way' :
        destination.allWays[child.get("id")] = child

        if tags.hasTags( child) :
            #  then translate then send to target
            tags.translateTags( child, translations)
#            print "iterating over destinations for way: "
            for d in destinations:
#                print "trying destination " + d.getFile()
                if d.isMatch( child):
#                    print "adding way to target " + d.getFile()
                    d.addWay( child)
#        else :
#            print "tagless way " + child.get('id')
    elif child.tag == 'relation' :
        tags.translateTags( child, translations)
#        print "iterating over destinations for relation: "
        for d in destinations:
#            print "trying destination " + d.getFile()
            if d.isMatch( child):
#                print "adding relation to target " + d.getFile()
                d.addRelation( child)
    else :
        log.error( "unrecognized element type")

for destination in destinations:
    destination.writeResults( )
