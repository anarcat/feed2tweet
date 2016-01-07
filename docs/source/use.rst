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
In order to increase the verbosity of what's Feed2tweet is doing, use the **--debug** option followed by the level of verbosity see [the the available different levels](https://docs.python.org/2/library/logging.html)::

    $ feed2tweet --debug debug -c /path/to/feed2tweet.ini
