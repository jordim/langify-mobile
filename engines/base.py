from abc import ABC, abstractmethod
import os

class EngineBase(ABC):

    def __init__(self):
        self.cached = {}
        self.output_file = self.output()
        self.input_file = self.input()
        self.output_folder = 'outputs'
        self.input_folder = 'inputs'

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def parse(self):
        pass

    def write(self,lang,data):
        output_file = '{}/{}/{}'.format(self.output_folder,lang,self.output_file)
        output_folder = '{}/{}'.format(self.output_folder,lang)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        with open(output_file,'w') as file:
            for k,v in data.items():
                line = self.generate_line(k,v)
                file.write(line)
                file.write("\n")
        file.close()
        pass

    @abstractmethod
    def generate_line(k,v):
        pass

    @abstractmethod
    def data(self):
        pass

    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def input(self):
        pass
