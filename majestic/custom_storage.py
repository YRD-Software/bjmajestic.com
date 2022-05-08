from storages.backends.azure_storage import AzureStorage

class PublicAzureStorage(AzureStorage):
    account_name = 'myaccount'
    account_key = 'mykey'
    azure_container = 'mypublic_container'
    expiration_secs = None