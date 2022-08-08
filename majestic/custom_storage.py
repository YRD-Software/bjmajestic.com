from storages.backends.azure_storage import AzureStorage


class StaticAzureStorage(AzureStorage):
    """StaticAzureStorage: Configure Azure storage for static files.

    Args:
        AzureStorage (Storage): Azure's storage class.
    """
    azure_container = 'static'


class MediaAzureStorage(AzureStorage):
    """MediaAzureStorage: Configure Azure storage for media files.

    Args:
        AzureStorage (Storage): Azure's storage class.
    """
    azure_container = 'media'
