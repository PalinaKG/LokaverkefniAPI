try:
    from .local_settings import *
except ImportError:
    pass

CORS_ORIGIN_ALLOW_ALL = True