## Solution Steps ##

1. Install ZipKin and have it up and running
2. Feed false data to mysqlite database.
3. Replace false data generation layer with python varnish logger.


## Tracking Micro-Services via Varnish Cache ##

Track timing of micro-service requests by passing micro-service requests through a varnish server.

* [Configuring JDK](docs/Configuring JDK.md)
* [ZipKin](docs/ZipKin.md)
* [Creating Services](docs/RPC Services.md)
  * [Example Service](docs/Example Service.md)
    * [Bash Script](script.sh)
     * be sure to change chmod +x script.sh, so you can run it as ``$> ./script.sh``
     * use ``$> terminate=1 ./script.sh`` to only terminate services. It will exit without creating any new services.
* [Structure of ZipKin tables and generating false data](docs/False data.md)
* [Varnish Logger](docs/Varnish Logger.md)


#### Machine Used ####

Debian 8.1 / **specifically** Linux debian 3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt9-3~deb8u1 (2015-04-24) x86_64 GNU/Linux
