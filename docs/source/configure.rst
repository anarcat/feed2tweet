Configure Feed2tweet
====================

As a prerequisite to use Feed2tweet, you need a Twitter app. Log in Twitter, go to https://apps.twitter.com, create an app and generate the access token.

In order to configure Feed2tweet, you need to create a feed2tweet.ini file (or any name you prefer, finishing with the extension .ini) with the following parameters::

    [twitter]
    consumer_key=ml9jaiBnf3pmU9uIrKNIxAr3v
    consumer_secret=8Cmljklzerkhfer4hlj3ljl2hfvc123rezrfsdctpokaelzerp
    access_token=213416590-jgJnrJG5gz132nzerl5zerwi0ahmnwkfJFN9nr3j
    access_token_secret=3janlPMqDKlunJ4Hnr90k2bnfk3jfnwkFjeriFZERj32Z

    [cache]
    cachefile=/home/user/feed2tweet/cache.db
    cache_limit=10000

    [rss]
    uri: https://www.journalduhacker.net/rss
    uri_list: /home/user/feed2tweet/rsslist.txt
    tweet: {title} {link}
    title_pattern: Open Source
    title_pattern_case_sensitive: true

    [hashtaglist]
    several_words_hashtags_list: /home/user/feed2tweet/hashtags.txt

For the [twitter] section:

- consumer_key: the Twitter consumer key (see your apps.twitter.com webpage)
- consumer_secret: the Twitter consumer secret key (see your apps.twitter.com webpage)
- access_token: the Twitter access token key (see your apps.twitter.com webpage)
- access_token_secret: the Twitter access token secret key (see your apps.twitter.com webpage)

For the [cache] section:

- cachefile: the path to the cache file storing ids of already tweeted links. Absolute path is mandatory. This file should always use the .db extension.
- cache_limit: length of the cache queue. defaults to 100.

For the [rss] section:

- uri: the url of the rss feed to parse
- uri_list: a path to a file with several adresses of rss feeds, one by line. Absolute path is mandatory.
- tweet: format of the tweet you want to post. It should use existing entries of the RSS fields like {title} or {link}. Launch it with this field empty to display all available entries.
- {one field of the rss feed}_pattern: takes a string representing a pattern to match for a specified field of each rss entry of the rss feed, like title_pattern or summary_pattern.
- {one field of the rss feed}_pattern_case_sensitive: either the pattern matching for the specified field should be case sensitive or not. Default to true if not specified.

For the [hashtaglist] section:

- several_words_hashtags_list: a path to the file containing hashtags in two or more words. Absolute path is mandatory. By default Feed2tweet adds a # before every words of a hashtag.

How to display available sections of the rss feed
=================================================
Starting from 0.8, Feed2tweet offers the **--rss-sections** command line option to display the available section of the rss feed and exits::

    $ feed2tweet --rss-sections -c feed2tweet.ini
    The following sections are available in this RSS feed: ['title', 'comments', 'authors', 'link', 'author', 'summary', 'links', 'tags', id', 'author_detail', 'published'].
