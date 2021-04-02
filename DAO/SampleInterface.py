from abc import ABCMeta, abstractmethod

class Interface(metaclass=ABCMeta):

    @abstractmethod
    def methodOne(self):
        pass

    @abstractmethod
    def methodTwo(self):
        pass

    @abstractmethod
    def methodThree(self):
        pass