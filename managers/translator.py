from google.cloud import translate

class TranslateManager(object):

    def __init__(self,params={}):
        self.params = params
        self.cached = {}
        self.client = translate.Client()

    def translate(self,word,lang):
        translation = self.client.translate(word,target_language=lang)
        value = translation['translatedText']
        self.cached[word] = value
        return value
