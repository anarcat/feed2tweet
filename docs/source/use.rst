Use Feed2tweet
==============
After the configuration of Feed2tweet, just launch the following command::

    $ feed2tweet -c /path/to/feed2tweet.ini

Test option
===========
In order to know what's going to be sent to Twitter without actually doing it, use the **--dry-run** option::

    $ feed2tweet --dry-run -c /path/to/feed2tweet.ini

Debug option
============
In order to increase the verbosity of what's Feed2tweet is doing, use the **--debug** option followed by the level of verbosity see [the the available different levels](https://docs.python.org/3/library/logging.html)::

    $ feed2tweet --debug -c /path/to/feed2tweet.ini

Run Feed2tweet on a regular basis
=================================
Feed2tweet should be launche on a regular basis in order to efficiently send your new RSS entries to Twitter. It is quite easy to achieve with adding a line to your user crontab, as described below::

    @hourly feed2tweet -c /path/to/feed2tweet.ini

will execute feed2tweet every hour. Or without the syntactic sugar in the global crontab file /etc/crontab::

    0 * * * * johndoe feed2tweet -c /path/to/feed2tweet.ini
