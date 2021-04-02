
class Headlines(object):

    def __init__(self):
        self.uuid = None
        self.author = None
        self.title = None
        self.query = None

    def getHeadlineId(self):
        return self.uuid

    def setHeadlineId(self, uuid):
        self.uuid = uuid

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getQuery(self):
        return self.query

    def setQuery(self, query):
        self.query = query