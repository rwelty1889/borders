import logging as log
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

def xstr( entity):
    if( entity == None):
        return "None"
    return str(entity)


def hasTags( element):
    """
    check on whether element has osm tags in its children.
    This is needed because, in the output from ogr2osm, some ways
    are closed, standalone and have tags, and the rest of the ways
    are open, part of relations and do not have tags.
    """
    for child in element:
        if child.tag == 'tag':
            return True
    return False


# translation list will be a list of original tag/value pairs to match,
# an action, and if needed the target values to add or substitute
# actions:
#  rename-key
#  rename-value
#  new-kv
#  delete-kv

def translateTags( element, translations):
    """convert tags to targeted set"""
#    print "translating tags for " + element.tag + " " + element.get('id')
    for translation in translations:
        translation.translateElement( element)
            
    return

class Tag:
    def __init__( self, k, v):
        self.key = k
        self.value = v

    def getKey( self):
        return self.key

    def getValue( self):
        return self.value

    def isMatch( self, k, v):
        return self.key == k \
            and (self.value == None or self.value == v)

    def findElement( self, element):
        for child in element:
            if self.isMatch( child.get('k'), child.get('v')):
#                print "hit! " + child.get('k') + " " + child.get('v')
                return child
        return None

    def printElementTags( self, element):
        print "element tags: "
        for child in element:
            if child.get('k'):
                print "k, v: " + child.get('k') + ' ' + child.get('v')

        return None

class tagTranslation:
    def __init__(self, origkey, origval, act, targkey, targval):
        self.originalTag = Tag( origkey, origval)
        self.targetTag = Tag( targkey, targval)
        self.action = act

    def matchKV( self, key, value):
        return self.originalTag.isMatch( key, value)

    def findElement( self, element):
        #loop over KV pairs until match found
        for child in element:
            if self.matchKV( child.get('k'), child.get('v')) :
                return child
        return None

    def translateElement( self, parent):
        element = self.findElement( parent)

        if element == None:
            return
#        print "executing action " + self.action + " on " + element.get( "v")
        if self.action == "rename-key":
            element.set( "k", self.targetTag.getKey())
        elif self.action == "rename-value":
            element.set( "v", self.targetTag.getValue())
        elif self.action == "new-kv":
            newTag = etree.Element( "tag")
            newTag.set( "k", self.targetTag.getKey())
            newTag.set( "v", self.targetTag.getValue())
            parent.append( newTag)
        elif self.action == "delete-kv":
            parent.remove( element)
