#!/usr/bin/env python
import sys
import os.path
import time
import json

# Figure out where we're installed
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BIN_DIR)

# Make sure that carbon's 'lib' dir is in the $PYTHONPATH if we're running from
# source.
LIB_DIR = os.path.join(ROOT_DIR, "lib")
sys.path.insert(0, LIB_DIR)

from settings import settings
from whisper_reader import WhisperReader

from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

def path_to_fs_path(path):
	fs_path = os.path.join(*path.split("."))
	fs_path = os.path.join(settings.STORAGE_DIR, fs_path)
	return fs_path + ".wsp"

class CarbonServerProtocol(LineReceiver):
	def lineReceived(self, line):
		(action, args) = line.split(" ",1)
		if (action == 'get_metric'):
			(path, start, end) = args.split(" ")
			fs_path = path_to_fs_path(path)
			reader = WhisperReader(fs_path, path)
			result = reader.fetch(int(start),int(end))
			self.sendLine(json.dumps(result))
		else:
			self.sendLine(json.dumps({'status': 'NOT OK'}))

class CarbonServerFactory(Factory):
	def buildProtocol(self,addr):
		return CarbonServerProtocol()

def main():
    """This runs the protocol on port 8024"""
    factory = CarbonServerFactory()
    reactor.listenTCP(8024,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()