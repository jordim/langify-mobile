import re
import os
from engines.base import EngineBase

class EngineAndroid(EngineBase):

    def __init__(self):
        super().__init__()

    def persist_file(self,file,data):
        for k,v in data.items():
            file.write(self.generate_line(k,v))
            file.write("\n")

    def format(self):
        return "<string name=\"#key#\">#value#</string>"

    def parse(self):
        target = '{}/{}'.format(self.input_folder,self.input_file)
        with open(target,'r') as file:
            for line in file.readlines():
                result = re.match("(<string name=\")(.*)(\">)(.*)(<\/string>)", line.strip())
                if result:
                    key = result.group(2)
                    value = result.group(4)
                    self.cached[key] = value

        return self.cached

    def generate_line(self, k,v):
        return self.format().replace("#key#",k).replace("#value#",v)

    def data(self):
        return self.cached

    def output(self):
        return 'android.xml'

    def input(self):
        return 'android.xml'
