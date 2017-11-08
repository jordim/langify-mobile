import json

from engines.ios import EngineIOS
from engines.android import EngineAndroid
from managers.translator import TranslateManager

from tabulate import tabulate

class CoreManager(object):

    def __init__(self,params):
        self.params = params
        self.data = {}
        self.translated = {}
        self.input_engine = None
        self.output_engines = []
        self.langs = params.get('langs',[])
        self.translate_manager = TranslateManager(langs=self.langs)
        self.engine_builder()

    def process(self):
        self.data = self.input_engine.parse()

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
        self.process()
        for lang in self.langs:
            specific_lang = {}
            for k,v in self.data.items():
                specific_lang[k] = word = self.translate_manager.translate(k,v,lang)
            self.translated[lang] = specific_lang
            for engine in self.output_engines:
                engine.write(lang,self.translated[lang])


    def engine_builder(self):
        targets = self.params.get('targets',[])
        for target in targets:
            engine = self.select_engine(target)
            self.output_engines.append(engine)

        input = self.params.get('input',None)
        self.input_engine = self.select_engine(input)

    def select_engine(self,target):
        if target == 'ios': return EngineIOS()
        elif target == 'android': return EngineAndroid()
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
            translations = self.translate_manager.translations_for_key(k)
            translations.insert(0,k)
            table.append(translations)
        print(tabulate(table))
