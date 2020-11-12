=================
nethserver-evebox
=================

EveBox configuration for NethServer:

- it requires nethserver-suricata
- it runs as ``suricata`` user, only if ``/var/log/suricata/eve.json`` file exists
- Suricata must be running and eve log must be enabled
- it uses SQLite
- no ElasticSearch support
- listens on port 5636, accessible only from localhost
- web interface served via reverse proxy: ``https://<host>:980/<alias>`` (see ``alias`` prop below)
- once a week internal GeoIP database is updated by a cron job

Properties:

- ``Retention``: positive integer, if greater than 0, events will be discarded after the given number of days 
- ``PublicAccess``: can be ``enabled`` or ``disabled``. If ``disabled``, access to evebox UI will be restricted only to trusted networks
- ``alias``: it is a random path generated once on first install and it will be used to compose evebox UI URL.

Database: ::

 evebox=service
    TCPPort=5636
    access=
    alias=be771675da40887ccf9eb98d05b88dc80559b6a6
    PublicAccess=enabled
    Retention=30
    status=enabled

Restrict access
===============

As default evebox is accessible from all IP addresses.
To restrict the access only from local and trusted networks use: ::

  config setprop evebox PublicAccess disabled
  signal-event nethserver-evebox-update


Links
=====

- Official site: https://evebox.org/
