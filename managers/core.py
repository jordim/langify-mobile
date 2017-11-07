from engines.ios import EngineIOS
from engines.android import EngineAndroid
from managers.translator import TranslateManager

class CoreManager(object):

    def __init__(self,params):
        self.params = params
        self.cached = {}
        self.translated = {}
        self.input_engine = None
        self.output_engines = []
        self.langs = params.get('langs',[])
        self.translate_manager = TranslateManager()
        self.engine_builder()

    def process(self):
        self.cached = self.input_engine.parse()

    def data(self):
        return self.cached

    def translate(self):
        self.process()
        for lang in self.langs:
            specific_lang = {}
            for k,v in self.cached.items():
                word = self.translate_manager.translate(v,lang)
                specific_lang[k] = word
            self.translated[k] = specific_lang
            for engine in self.output_engines:
                engine.write(lang,self.translated[k])


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
