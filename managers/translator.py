from google.cloud import translate

from managers.cache import CacheManager

class TranslateManager(object):

    def __init__(self,langs=[]):
        self.langs = langs
        self.client = translate.Client()
        self.cache_manager = CacheManager()

    def translate(self,item):
        cached_value = self.cache_manager.get(item)
        if cached_value is None:
            translation = self.client.translate(item.value,target_language=item.lang)
            item.value = translation['translatedText']
            self.cache_manager.save(item)
        else:
            return cached_value

        return item.value

    def translations_for_key(self,item):
        temp = []
        for lang in self.langs:
            item.lang = lang
            translation = self.cache_manager.get(item)
            if translation:
                temp.append(translation)
        return temp

    def finalize(self):
        self.cache_manager.persist()
