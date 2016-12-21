Plugins
=======
Starting from 0.9, Feed2tweet now supports plugins. Plugins offer optional features, not supported by default. Optional means you need a dedicated configuration and sometimes a dedicated external dependencies. What you need for each module is specified below.

InfluxDB
--------
The InfluxDB plugin allows to store already published tweets in a InfluxDB database.

Install the InfluxDB plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^
To install Feed2tweet with the InfluxDB plugin, execute the following command.

From scratch::

    # pip3 install feed2tweet[influxdb]

Upgrading from a previous version, execute the followin command::

    # pip3 install feed2tweet[influxdb] --upgrade

Configuration
^^^^^^^^^^^^^
Below is the block of configuration to add in your feed2tweet.ini::

    [influxdb]
    ;host=127.0.0.1
    ;port=8086
    user=influxuser
    pass=V3ryS3cr3t
    database=influxdb
    measurement=tweets

- host: the host where the influxdb instance is. Defaults to 127.0.0.1
- port: the port where the influxdb instance is listening to. Defaults to 8086
- user: the user authorized to connect to the database. Mandatory (no default)
- pass: the password needed to connect to the database. Mandatory (no default)
- database: the name of the influxdb database to connect to. Mandatory (no default)
- measurement: the measurement to store the value into. Mandatory (no default)
