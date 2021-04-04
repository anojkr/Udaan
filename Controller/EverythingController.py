

class EverthingController(object):

    def __init__(self, DaoObject):
        self.DaoObject = DaoObject

    def CreateEverything(self, uuid, author, title, query):
        response = self.DaoObject.CreateEverything(uuid, author, title, query)
        return response.uuid

    def GetEverything(self, uuid):
        response = self.DaoObject.GetEverything(uuid)
        return response
