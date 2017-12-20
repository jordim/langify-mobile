import re
import os
import json
from engines.base import EngineBase

class EngineIonic(EngineBase):

    def __init__(self):
        super().__init__()
        self.type = 'json'

    def persist_file(self,file,data):
        json.dump(data, file,ensure_ascii=False).encode('utf8')

    def format(self):
        pass

    def parse(self):
        target = '{}/{}'.format(self.input_folder,self.input_file)
        with open(target,'r') as json_file:  
            data = json.load(json_file)
            for k,v in data.items():
                self.cached[k] = v
        return self.cached

    def generate_line(self, k,v):
        return {k:v}

    def data(self):
        return self.cached

    def output(self):
        return 'ionic.json'

    def input(self):
        return 'ionic.json'
