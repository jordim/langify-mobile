from abc import ABCMeta, abstractmethod

class EngineBase(metaclass=ABCMeta):

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def write(self,data):
        pass

    @abstractmethod
    def data(self):
        pass
