import re
import os

from engines.base import EngineBase

class EngineIOS(EngineBase):

    def __init__(self):
        super().__init__()

    def parse(self):
        target = '{}/{}'.format(self.input_folder,self.input_file)
        with open(target,'r') as file:
            for line in file.readlines():
                result = re.match("\"(.*)\"(\s+=\s+)\"(.*)\"", line.strip())
                if result:
                    key = result.group(1)
                    value = result.group(3)
                    self.cached[key] = value

        return self.cached

    def format(self):
        return "\"#key#\" = \"#value#\";"

    def generate_line(self,k,v):
        return self.format().replace("#key#",k).replace("#value#",v)

    def data(self):
        return self.cached

    def output(self):
        return 'ios.localizable'

    def input(self):
        return 'ios.strings'
