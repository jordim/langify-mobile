import re
import os
from engines.base import EngineBase

class EngineAndroid(EngineBase):

    def __init__(self):
        self.input_file = 'inputs/android.strings'
        self.output_folder = 'outputs'
        self.output_file = 'values.strings'
        self.cached = {}

    def format(self):
        return "<string name=\"#key#\">#value#</string>"

    def parse(self):
        with open(self.input_file,'r') as file:
            for line in file.readlines():
                result = re.match("(<string name=\")(.*)(\">)(.*)(<\/string>)", line.strip())
                if result:
                    key = result.group(1)
                    value = result.group(3)
                    self.cached[key] = value

        return self.cached

    def write(self,lang,data):
        output_file = '{}/{}/{}'.format(self.output_folder,lang,self.output_file)
        output_folder = '{}/{}'.format(self.output_folder,lang)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        with open(output_file,'w') as file:
            for k,v in data.items():
                line = self.format().replace("#key#",k).replace("#value#",v)
                file.write(line)
                file.write("\n")
        file.close()


    def data(self):
        return self.cached
