import re
import glob
import os
import json
from engines.base import EngineBase

class EngineTXT(EngineBase):

    def __init__(self):
        super().__init__()
        self.type = 'txt'

    def persist_file(self,file,data):
        json.dump(data, file, ensure_ascii=False, indent=4, separators=(',', ': '))

    def format(self):
        pass

    def parse(self):
        for file in glob.glob("inputs/*.txt"):
            target = '{}/{}'.format(self.input_folder,file)
            with open(file,'r') as f:
                self.cached[file] = f.read()
            f.close()
        return self.cached

    def generate_line(self, k,v):
        return {k:v}

    def data(self):
        return self.cached

    def output(self):
        return 'txt.json'

    def input(self):
        pass
