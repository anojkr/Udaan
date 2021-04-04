
class Source(object):

    def __init__(self):
        self.uuid = None
        self.name = None
        self.description = None

    def getSourceId(self):
        return self.uuid

    def setSourceId(self, uuid):
        self.uuid = uuid

    def getSourceName(self):
        return self.name

    def setSourceName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

