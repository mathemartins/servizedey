import datetime
AWS_ACCESS_KEY_ID = "AKIAIZI4KSZTYRN7BRVQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'dev.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'dev.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'servizedey'
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
PROTECTED_URL = '//%s.s3.amazonaws.com/media/protected/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
PROTECTED_ROOT = PROTECTED_URL

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}