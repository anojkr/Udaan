from Models.SourceModels import Source
from DAO.SourceInterface import SourceInterface

class SourceDAO(SourceInterface):

    records = {}
    def CreateSource(self, uuid, name, desc):

        object = Source()
        object.setSourceId(uuid)
        object.setSourceName(name)
        object.setDescription(desc)

        self.__class__.records[uuid] = object
        return object

    def GetSource(self, uuid):
        return self.__class__.records[uuid]