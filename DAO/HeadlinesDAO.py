from Models.HeadlinesModels import Headlines
from DAO.HeadlinesInterface import HeadlinesInterface


class HeadlinesDAO(HeadlinesInterface):
    records = {}

    def CreateHeadlines(self, uuid, author, title, query):
        object = Headlines()
        object.setHeadlineId(uuid)
        object.setAuthor(author)
        object.setTitle(title)
        object.setQuery(query)
        self.__class__.records[uuid] = object

        return object

    def GetHeadlines(self, uuid):
        return self.__class__.records[uuid]
