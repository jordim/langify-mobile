import json
import os

class CacheItem(object):

    def __init__(self,key=None,value=None,lang=None):
        self.key = key
        self.value = value
        self.lang = lang

class CacheManager(object):

    def __init__(self):
        self.file_name = 'cached.json'
        self.cache = {}
        self.load()

    def get(self,item):
        lang = item.lang
        key = item.key
        cache_lang = self.cache.get(lang,{})
        return cache_lang.get(key, None)

    def save(self,item):
        cache_lang = self.cache.get(item.lang,{})
        cache_lang[item.key] = item.value
        self.cache[item.lang] = cache_lang

    def persist(self):
        with open(self.file_name,'w') as file:
            json.dump(self.cache,file)

    def load(self):
        if self.cache_exists():
            with open(self.file_name) as file:
                self.cache = json.load(file)

    def cache_exists(self):
        return os.path.isfile(self.file_name)
