'''
representation of targets for split data

'''
from lxml import etree
import time
import datetime
import pytz

# all nodes indexed by id
allNodes = {} 

# all ways without tags
allWays = {}

class Target:
    def __init__(self, f, t):
        self.file = f
        self.tags = t
        self.tree = etree.ElementTree()
        self.rootElement \
             = etree.Element("osm", \
                             generator="splitter", \
                             upload="true", \
                             version="0.6")
        self.tree._setroot( self.rootElement)
        # nodes value is id
        self.nodes = set()
        # ways value is id
        self.ways = set()
        # relations key is the relations id, value is the entity from xml
        self.relations = {}

    def getFile( self):
        return self.file

    def addNode( self, nodeid):
        if not nodeid in self.nodes:
            self.nodes.add( nodeid)
            node = allNodes[nodeid]
            element = etree.Element("node")
            attributes = node.attrib
            for attrkey in attributes.keys():
                if attrkey == 'id':
                    element.set(attrkey, str( - int( node.get(attrkey))))
                else:
                    element.set(attrkey, node.get(attrkey))
            element.set( 'version', '1')
            element.set( 'timestamp', datetime.datetime.now(pytz.utc).isoformat())
            self.rootElement.append( element)

    def addWay( self, way):
        self.ways.add(way.get('id'))
        for child in way:
            if child.tag == 'nd':
               self.addNode( child.get( "ref"))

    def addRelation( self, relation):
        self.relations[relation.get('id')] = relation
        for child in relation:
            if child.tag == 'member':
                self.addWay( allWays[child.get('ref')])

    def isMatch( self, element):
        for tag in self.tags:
            for child in element:
                if tag.isMatch( child.get('k'), child.get('v')):
                    return True
        return False
#            print tag.printElementTags( element)
#            ele = tag.findElement( element)
#            if ele :
#
#            if tag.findElement( element):
#                print "hit! 2"
#                return True
#    return False

    def shallowCopy( self, entity):
        element = etree.Element( entity.tag)
        attributes = entity.attrib
        for attrkey in attributes.keys():
            if (entity.tag == 'nd' or entity.tag == "member") \
               and attrkey == 'ref':
                element.set(attrkey, str( - int( entity.get(attrkey))))
            else:
                element.set(attrkey, entity.get(attrkey))
        return element

    def writeEntity( self, entity):
        element = etree.Element( entity.tag)
        attributes = entity.attrib
        for attrkey in attributes.keys():
            if attrkey == 'id':
                element.set(attrkey, str( - int( entity.get(attrkey))))
            else:
                element.set(attrkey, entity.get(attrkey))
        for child in entity:
            childCopy = self.shallowCopy( child)
            element.append( childCopy)
        element.set( 'version', '1')
        element.set( 'timestamp', datetime.datetime.now(pytz.utc).isoformat())
        self.rootElement.append( element)
        return

    def writeResults(self):

        # nodes & headers are already set up

        if len( self.ways) > 0 or len( self.relations) > 0:
            # iterate over ways
            for wayid in self.ways:
                way = allWays[wayid]
                self.writeEntity( way)

            # iterate over relations
            for relation in self.relations.values(): # need values
                self.writeEntity( relation)
            # write result
            self.tree.write( self.file, pretty_print=True)

        else:
            print "no ways or relations, skipping " + self.file
        return
