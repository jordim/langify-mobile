from managers.core import CoreManager

#example
params = {
    'input' : 'android',
    'targets' : ['ios','android'],
    'langs' : ['it','fr'],
}
core_manager = CoreManager(params)
core_manager.translate()

#export GOOGLE_APPLICATION_CREDENTIALS="service_account.json"
