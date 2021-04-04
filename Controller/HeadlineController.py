

class HeadlineController(object):

    def __init__(self, DaoObject):
        self.DaoObject = DaoObject

    def createHeadlines(self, uuid, author, title, query):
        response = self.DaoObject.CreateHeadlines(uuid, author, title, query)
        return response.uuid

    def GetHeadlines(self, uuid):
        response = self.DaoObject.GetHeadlines(uuid)
        return response
