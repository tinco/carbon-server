from yaml import load
from collections import namedtuple
from struct import Struct

f = open('settings.yml','r')
r = f.read()
f.close()
settings_dict = load(r)

class Settings:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

settings = Settings(**settings_dict)

# class Settings(object):
#     LOG_DIR = "log"
#     LOG_RENDERING_PERFORMANCE = False
#     LOG_METRIC_ACCESS = False
#     STORAGE_DIR = "/home/phusion/Source/carbon/storage/whisper"

#     # Cluster settings
#     CLUSTER_SERVERS = []
#     REMOTE_FIND_TIMEOUT = 3.0
#     REMOTE_FETCH_TIMEOUT = 6.0
#     REMOTE_RETRY_DELAY = 60.0
#     REMOTE_READER_CACHE_SIZE_LIMIT = 1000
#     CARBONLINK_HOSTS = ["127.0.0.1:7002"]
#     CARBONLINK_TIMEOUT = 1.0
#     CARBONLINK_HASHING_KEYFUNC = None
#     CARBONLINK_RETRY_DELAY = 15
#     REPLICATION_FACTOR = 1
#     MEMCACHE_HOSTS = []
#     FIND_CACHE_DURATION = 300
#     FIND_TOLERANCE = 2 * FIND_CACHE_DURATION
#     DEFAULT_CACHE_DURATION = 60 #metric data and graphs are cached for one minute by default
#     LOG_CACHE_PERFORMANCE = True

# settings = Settings()