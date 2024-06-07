from django.core.exceptions import ValidationError
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# if use media storage
class MediaStorage(S3Boto3Storage):
    location = ""
    file_overwrite = False

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(MediaStorage, self).__init__(*args, **kwargs)
