from abc import ABC, abstractmethod
import os
import json 
import logging

logger = logging.getLogger('langify')

class EngineBase(ABC):
    """Abstract class that represents an Engine to parse and write the transaltions for each platform"""
    def __init__(self):
        self.type = 'text'
        self.cached = {}
        self.output_file = self.output()
        self.input_file = self.input()
        self.output_folder = 'outputs'
        self.input_folder = 'inputs'

    def write(self,lang,data):
        """Write a translated file for a specific platform"""
        output_file = '{}/{}/{}'.format(self.output_folder,lang,self.output_file)
        output_folder = '{}/{}'.format(self.output_folder,lang)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        print(os.path.abspath(output_folder))
        with open(output_file,'w') as file:
            self.persist_file(file,data)
            logger.info("({}) => {}".format(lang,os.path.abspath(output_file)))
        file.close()
        pass


    @abstractmethod
    def persist_file(self,file,data):
        """Process all key values and persist to a file"""

        pass

    @abstractmethod
    def format(self):
        """Return the format of the lines of the localizable files for each platform"""

        pass

    @abstractmethod
    def parse(self):
        pass


    @abstractmethod
    def generate_line(k,v):
        """Return a translated line for a specific platform"""

        pass

    def data(self):
        """Return a dictionary where key is the language and its value is a dictionary of key values with translated words"""

        return self.data

    @abstractmethod
    def output(self):
        """Return the filename of the file we want to write with translations done"""
        
        pass

    @abstractmethod
    def input(self):
        """Return the filename of the file that we want to translate"""

        pass
