=======
Zipnish
=======

Microservice monitoring tool based on Varnish-Cache_. Currently it only supports Varnish 4.
Zipnish piggybacks the VSL_ and stores a bunch of data in a similar way as Zipkin_ does.

There is a log-reader component responsible for fetching data from VSL_ and having it stored into a MySql database,
furthermore there is an available UI that will display in a hierachical manner all requests going
through varnish to your services. Both of these components share the same MySql instance.

.. _VSL: https://www.varnish-cache.org/docs/4.0/reference/vsl.html
.. _Zipkin: http://zipkin.io/
.. _Varnish-Cache: https://varnish-cache.org/

Prerequisites
=============

Following packages are required for running Zipnish:

    * simplemysql
    * flask
    * sqlalchemy
    * flask_sqlalchemy
    * mysql-python

Installation
============

Install with pip::

    $ sudo pip install zipnish

Configuration
=============

A configuration file found at ``/etc/zipnish/zipnish.cfg`` is required with a structure as described below:

.. code-block:: sh

    [Database]
    # Db settings for the MySql connection.

    # MySql host
    host = 192.168.59.103

    # Database name
    db_name = microservice

    # User name
    user = zipnish

    # Password
    pass = secret

    # Connection keep-alive
    keep_alive = true

    [Cache]
    # Defines which cache to fetch logs from.
    # Name of the cache (same value sent via the -n argument)
    # name = demo

    [Log]
    # Path to the daemon logfile.
    log_file = /var/log/zipnish/zipnish.log

    # Valid log_levels are: DEBUG, INFO, WARNING, ERROR
    log_level = DEBUG

For convenience purposes, there is a docker image available which handles setting up Mariadb database along with a test user.

Run Zipnish
===========

Considering that your Varnish instance is properly configured in relation to your services, after installing Zipnish
there are two commands available:

Run the logreader::

    $ zipnish-logreader


Run the ui (by default port 5000)::

    $ zipnish-ui

Contents:


.. toctree::
   :maxdepth: 1

   ui
   vcl
   docker
   examples
   tutorial
   changes
