Carbon Server
=============

A simple interface to retrieve data from a whisper database with a carbon cache.



Steps for integrating this into carbon-cache
---------------

  - add `carbon-server.py` to  `bin/`
  - add `carbon_server_plugin.py` to `lib/twisted/plugins/`
  - add service creator to `lib/carbon/service.py`
  - add protocol factory to `lib/carbon/protocols.py`
  - add dependencies as needed to `lib/carbon`

Credits
-------
Present and past members of the Graphite team (https://github.com/graphite-project?tab=members)
Phusion (http://phusion.nl)