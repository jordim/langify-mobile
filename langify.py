from managers.core import CoreManager

import fire

def translate(name="World",
          i=None,  #input engine ej: 'android'
          t='',    #output engine ej: 'android,ios'
          langs='',
          c=False, #cache
          p=True,  #print table results
          l=False):

    params = {
        'input': i,
        'targets': list(t),
        'langs': list(langs),
        'save_cache': c,
        'print_table': p,
        'log': l
    }
    core_manager = CoreManager(params)
    core_manager.translate()
    print(params)


if __name__ == '__main__':
    fire.Fire(translate)
