

class SourceController(object):

    def __init__(self, DaoObject):
        self.DaoObject = DaoObject

    def CreateSource(self, uuid, name, desc):
        response = self.DaoObject.CreateSource(uuid, name, desc)
        return response

    def GetSource(self, uuid):
        response = self.DaoObject.GetSource(uuid)
        return response
