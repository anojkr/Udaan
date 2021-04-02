from abc import ABCMeta, abstractmethod

class EverythingInterface(metaclass=ABCMeta):

    @abstractmethod
    def CreateEverything(self):
        pass

    @abstractmethod
    def GetEverything(self):
        pass

