from abc import ABCMeta, abstractmethod

class HeadlinesInterface(metaclass=ABCMeta):

    @abstractmethod
    def CreateHeadlines(self):
        pass

    @abstractmethod
    def GetHeadlines(self):
        pass

