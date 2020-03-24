import json

from engines.ios import EngineIOS
from engines.android import EngineAndroid
from engines.ionic import EngineIonic
from engines.txt import EngineTXT
from managers.translator import TranslateManager
from managers.cache import CacheItem

from tabulate import tabulate

import logging

logger = logging.getLogger('langify')

class CoreManager(object):

    def __init__(self,params):

        self.save_cache = params.get('save_cache',True)
        self.print_table = params.get('print_table',True)
        self.params = params
        self.data = {}
        self.translated = {}
        self.input_engine = None
        self.output_engines = []
        self.input = params.get('input', None)
        self.targets = params.get('targets',[])
        self.langs = params.get('langs',[])
        self.translate_manager = TranslateManager(langs=self.langs)
        self.engine_builder()

    def process_content_from_file(self):
        if self.input_engine:
            self.data = self.input_engine.parse()
        else:
            raise Exception("Wrong input engine")

    def keys(self):
        temp = {}
        for lang in self.langs:
            data = self.translated[lang]
            for k in data.keys():
                temp[k] = k
        return temp

    def data(self):
        return self.data

    def translate(self):
        self.process_content_from_file()
        for lang in self.langs:
            specific_lang = {}
            for k,v in self.data.items():
                item = CacheItem(k,v,lang)
                specific_lang[k] = word = self.translate_manager.translate(item)
            self.translated[lang] = specific_lang
            for engine in self.output_engines:
                engine.write(lang,self.translated[lang])
        if self.save_cache:
            self.finalize()
        if self.print_table:
            self.display()


    def engine_builder(self):
        """Read configuration and initalize all needed engines"""

        for target in self.targets:
            engine = self.select_engine(target)
            if engine:
                self.output_engines.append(engine)
       
        input = self.params.get('input',None)
        self.input_engine = self.select_engine(input)

    def select_engine(self,target):
        if target == 'ios': return EngineIOS()
        elif target == 'android': return EngineAndroid()
        elif target == 'ionic': return EngineIonic()
        elif target == 'txt': return EngineTXT()
        else: return None

    def finalize(self):
        self.translate_manager.finalize()

    def display(self):
        table = []
        lang_table = ['key']
        for lang in self.langs:
            lang_table.append(lang)
        table = [lang_table]
        for k in self.keys():
            item = CacheItem(key=k)
            translations = self.translate_manager.translations_for_key(item)
            translations.insert(0,k)
            table.append(translations)
