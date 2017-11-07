from managers.core import CoreManager

import config

core_manager = CoreManager(config.params)
core_manager.translate()

#export GOOGLE_APPLICATION_CREDENTIALS="service_account.json"
