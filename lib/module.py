import imp
from os.path import splitext, basename
import socket
import errno
import time
import sys

from os import environ

def load_module(module_path, member=None):
  module_name = splitext(basename(module_path))[0]
  module_file = open(module_path, 'U')
  description = ('.py', 'U', imp.PY_SOURCE)
  module = imp.load_module(module_name, module_file, module_path, description)
  if member:
    return getattr(module, member)
  else:
    return module