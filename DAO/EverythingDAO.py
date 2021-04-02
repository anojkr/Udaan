from Models.EverythingModels import Everything
from DAO.EverthingInterface import EverythingInterface


class EverythingDAO(EverythingInterface):
    records = {}

    def CreateEverything(self, uuid, author, title, query):
        object = Everything()
        object.setEverythingId(uuid)
        object.setAuthor(author)
        object.setTitle(title)
        object.setQuery(query)
        self.__class__.records[uuid] = object

        return object

    def GetEverything(self, uuid):
        return self.__class__.records[uuid]
