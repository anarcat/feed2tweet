Use Feed2tweet
==============
After the configuration of Feed2tweet, just launch the following command::

    $ feed2tweet -c /path/to/feed2tweet.ini

Run Feed2tweet on a regular basis
=================================
Feed2tweet should be launche on a regular basis in order to efficiently send your new RSS entries to Twitter. It is quite easy to achieve with adding a line to your user crontab, as described below::

    @hourly feed2tweet -c /path/to/feed2tweet.ini

will execute feed2tweet every hour. Or without the syntactic sugar in the global crontab file /etc/crontab::

    0 * * * * johndoe feed2tweet -c /path/to/feed2tweet.ini

Test option
===========
In order to know what's going to be sent to Twitter without actually doing it, use the **--dry-run** option::

    $ feed2tweet --dry-run -c /path/to/feed2tweet.ini

Debug option
============
In order to increase the verbosity of what's Feed2tweet is doing, use the **--debug** option followed by the level of verbosity see [the the available different levels](https://docs.python.org/3/library/logging.html)::

    $ feed2tweet --debug -c /path/to/feed2tweet.ini

Populate the cache file without posting tweets
==============================================
Starting from 0.8, Feed2tweet offers the **--populate-cache** command line option to populate the cache file without posting to Twitter::

    $ feed2tweet --populate-cache -c feed2tweet.ini
    populating RSS entry https://www.journalduhacker.net/s/65krkk
    populating RSS entry https://www.journalduhacker.net/s/co2es0
    populating RSS entry https://www.journalduhacker.net/s/la2ihl
    populating RSS entry https://www.journalduhacker.net/s/stfwtx
    populating RSS entry https://www.journalduhacker.net/s/qq1wte
    populating RSS entry https://www.journalduhacker.net/s/y8mzrp
    populating RSS entry https://www.journalduhacker.net/s/ozjqv0
    populating RSS entry https://www.journalduhacker.net/s/6ev8jz
    populating RSS entry https://www.journalduhacker.net/s/gezvnv
    populating RSS entry https://www.journalduhacker.net/s/lqswmz
