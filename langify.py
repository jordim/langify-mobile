import os

from managers.core import CoreManager

import config

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
core_manager = CoreManager(config.params)
core_manager.translate()
