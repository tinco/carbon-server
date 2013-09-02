#!/usr/bin/env python
import sys
import os.path
import time

# Figure out where we're installed
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BIN_DIR)

# Make sure that carbon's 'lib' dir is in the $PYTHONPATH if we're running from
# source.
LIB_DIR = os.path.join(ROOT_DIR, "lib")
sys.path.insert(0, LIB_DIR)

from whisper_reader import WhisperReader
# run our shit

reader = WhisperReader('/home/phusion/Source/carbon/storage/whisper/carbon/agents/tinco-a/cpuUsage.wsp','carbon.agents.tinco-a.cpuUsage')

start = time.time() - 3600
end = time.time()

(info, values) = reader.fetch(start,end)

print(values)