from abc import ABCMeta, abstractmethod

class SourceInterface(metaclass=ABCMeta):

    @abstractmethod
    def CreateSource(self):
        pass

    @abstractmethod
    def GetSource(self):
        pass

