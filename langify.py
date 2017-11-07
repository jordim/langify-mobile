import os

from managers.core import CoreManager

import config

os.system("export GOOGLE_APPLICATION_CREDENTIALS='service_account.json'")
core_manager = CoreManager(config.params)
core_manager.translate()
core_manager.finalize()
