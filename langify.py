from managers.core import CoreManager

import fire

import logging

logger = logging.getLogger('langify')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
logger.addHandler(ch)

def translate(name="World",
          i=None,  #input engine ej: 'android'
          t=None,    #output engine ej: 'android,ios'
          langs=None,
          c=False, #cache
          p=True  #print table results
    ):

    if i is None:
        raise Exception("Input is mandatory")

    if type(t) == tuple:
        t = list(t)
    elif type(t) == str:
        t = [i]
    else:
        t = [i]

    if type(langs) == tuple:
        langs = list(langs)
    elif type(langs) == str:
        langs = [langs]
    
    params = {
        'input': i,
        'targets': t,
        'langs': langs,
        'save_cache': c,
        'print_table': p
    }
    
    core_manager = CoreManager(params)
    core_manager.translate()

if __name__ == '__main__':
    fire.Fire(translate)
