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