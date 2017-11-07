import json
import os

class CacheManager(object):

    def __init__(self):
        self.file_name = 'cached.json'
        self.cache = {}
        self.load()

    def get(self,key,lang):
        cache_lang = self.cache.get(lang,{})
        return cache_lang.get(key, None)

    def save(self,key,value,lang):
        cache_lang = self.cache.get(lang,{})
        cache_lang[key] = value
        self.cache[lang] = cache_lang

    def persist(self):
        with open(self.file_name,'w') as file:
            json.dump(self.cache,file)

    def load(self):
        if self.cache_exists():
            with open(self.file_name) as file:
                self.cache = json.load(file)

    def cache_exists(self):
        return os.path.isfile(self.file_name)
