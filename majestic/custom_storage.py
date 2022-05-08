from storages.backends.azure_storage import AzureStorage

class StaticAzureStorage(AzureStorage):
    azure_container = 'static'
    azure_location = 'static'