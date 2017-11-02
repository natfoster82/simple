import os
from json import loads


SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_URL = 'redis://{0}:6379'.format(REDIS_HOST)
