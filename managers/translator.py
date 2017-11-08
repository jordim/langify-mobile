from google.cloud import translate

from managers.cache import CacheManager

class TranslateManager(object):

    def __init__(self,langs=[],params={}):
        self.params = params
        self.langs = langs
        self.client = translate.Client()
        self.cache_manager = CacheManager()

    def translate(self,key,value,lang):
        cached_value = self.cache_manager.get(key,lang)
        if cached_value is None:
            print(key,"in",lang,"was not cached")
            translation = self.client.translate(value,target_language=lang)
            value = translation['translatedText']
            self.cache_manager.save(key,value,lang)
        else:
            print(key,"in",lang,"was cached")
            return cached_value
        return value

    def translations_for_key(self,key):
        temp = []
        for lang in self.langs:
            translation = self.cache_manager.get(key,lang)
            if translation:
                temp.append(translation)
        return temp

    def finalize(self):
        self.cache_manager.persist()
