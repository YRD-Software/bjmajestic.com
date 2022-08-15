from storages.backends.s3boto3 import S3Boto3Storage


class StaticS3Storage(S3Boto3Storage):
    """StaticS3Storage: Configure S3 storage for static files.
    """
    location = 'static'
    default_acl = 'public-read'
    

class PublicMediaS3Storage(S3Boto3Storage):
    """PublicMediaS3Storage: Configure S3 storage for public media files.
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    
class PrivateMediaS3Storage(S3Boto3Storage):
    """PrivateMediaS3Storage: Configure S3 storage for private media files.
    """
    location = 'private'
    default_acl = 'private'
    file_overwrite = False