### Feed2tweet

Feed2tweet automatically parses rss feeds, identifies new posts and posts them on Twitter.
For the full documentation, [read it online](https://feed2tweet.readthedocs.org/en/latest/).

### Quick Install

* Install Feed2tweet from PyPI

        # pip3.4 install feed2tweet

* Install Feed2tweet from sources
  *(see the installation guide for full details)
  [Installation Guide](http://feed2tweet.readthedocs.org/en/latest/install.html)*


        # tar zxvf feed2tweet-0.3.tar.gz
        # cd feed2tweet
        # python3.4 setup.py install
        # # or
        # python3.4 setup.py install --install-scripts=/usr/bin

### Use Feed2tweet

* Create or modify feed2tweet.ini file in order to configure feed2tweet:

        [twitter]
        consumer_key=ml9jaiBnf3pmU9uIrKNIxAr3v
        consumer_secret=8Cmljklzerkhfer4hlj3ljl2hfvc123rezrfsdctpokaelzerp
        access_token=213416590-jgJnrJG5gz132nzerl5zerwi0ahmnwkfJFN9nr3j
        access_token_secret=3janlPMqDKlunJ4Hnr90k2bnfk3jfnwkFjeriFZERj32Z

        [cache]
        cachefile=cache.db

        [rss]
        uri=https://www.journalduhacker.net/rss

        [hashtaglist]
        several_words_hashtags_list=severalwordshashtaglist.txt

* Launch Feed2tweet

        $ feed2tweet -c /path/to/feed2tweet.ini

### Authors

Antoine Beaupré <anarcat@debian.org>
Carl Chenet <chaica@ohmytux.com>

First developed by Todd Eddy

### License

This software comes under the terms of the GPLv3+. Previously under MIT license. See the LICENSE file for the complete text of the license.
