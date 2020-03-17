import json

from engines.ios import EngineIOS
from engines.android import EngineAndroid
from engines.ionic import EngineIonic
from managers.translator import TranslateManager
from managers.cache import CacheItem

from tabulate import tabulate

class CoreManager(object):

    def __init__(self,params):
        self.save_cache = params.get('save_cache',True)
        self.print_table = params.get('print_table',True)
        self.params = params
        self.data = {}
        self.translated = {}
        self.input_engine = None
        self.output_engines = []
        self.langs = params.get('langs',[])
        self.translate_manager = TranslateManager(langs=self.langs)
        self.engine_builder()

    def process_content_from_file(self):
        if self.input_engine:
            self.data = self.input_engine.parse()
        else:
            print("Wrong input enigne")

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
        """Process and translate all files to specified languages and platforms"""

        self.process_content_from_file()
        for lang in self.langs:
            specific_lang = {}
            for k,v in self.data.items():
                item = CacheItem(k,v,lang)
                specific_lang[k] = word = self.translate_manager.translate(item)
                if(self.log()):
                    print(item.key," <---> ",item.lang," <---> ",item.value," <---> ",word)
            self.translated[lang] = specific_lang
            for engine in self.output_engines:
                engine.write(lang,self.translated[lang])
        if self.save_cache:
            self.finalize()
        if self.print_table:
            self.display()


    def engine_builder(self):
        """Read configuration and initalize all needed engines"""

        targets = self.params.get('targets',[])
        for target in targets:
            engine = self.select_engine(target)
            if engine:
                self.output_engines.append(engine)

        input = self.params.get('input',None)
        self.input_engine = self.select_engine(input)

    def select_engine(self,target):
        if target == 'ios': return EngineIOS()
        elif target == 'android': return EngineAndroid()
        elif target == 'ionic': return EngineIonic()
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
        print(tabulate(table))

    def log(self):
        return self.params['log']
