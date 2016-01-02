Configure Feed2tweet
====================

As a prerequisite to use Feed2tweet, you need a Twitter app. Log in
Twitter, go to `apps page <https://apps.twitter.com>`_, create an app
and generate the access token.

In order to configure Feed2tweet, you need to create a
``~/.config/feed2tweet.ini` file with the following parameters::

    [twitter]
    consumer_key=ml9jaiBnf3pmU9uIrKNIxAr3v
    consumer_secret=8Cmljklzerkhfer4hlj3ljl2hfvc123rezrfsdctpokaelzerp
    access_token=213416590-jgJnrJG5gz132nzerl5zerwi0ahmnwkfJFN9nr3j
    access_token_secret=3janlPMqDKlunJ4Hnr90k2bnfk3jfnwkFjeriFZERj32Z

For the [twitter] section:

- consumer_key: the Twitter consumer key (see your apps.twitter.com webpage)
- consumer_secret: the Twitter consumer secret key (see your apps.twitter.com webpage)
- access_token: the Twitter access token key, will be interactively
  generated if missing
- access_token_secret: the Twitter access token secret key, will also
  be interactively generated
