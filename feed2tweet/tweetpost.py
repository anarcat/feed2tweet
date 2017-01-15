# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
# Copyright © 2015-2016 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

"""Checks an RSS feed and posts new entries to twitter."""

# standard libraires imports
from configparser import SafeConfigParser, NoOptionError, NoSectionError
from argparse import ArgumentParser
import codecs
import logging
import os
import sys

# 3rd party libraries imports
import feedparser
import tweepy

class TweetPost(object):
    '''TweetPost class'''

    def __init__(self, config, tweet):
        '''Constructore of the TweetPost class'''
        self.config = config
        self.tweet = tweet
        self.main()

    @staticmethod
    def oauth_init(config, auth=None):
        '''initialise oauth access tokens

        will overwrite existing tokens without confirmation'''
        if auth is None:
            consumer_key = config.get('twitter', 'consumer_key')
            consumer_secret = config.get('twitter', 'consumer_secret')
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        logging.warning("Twitter access tokens need to be configured")
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            logging.error('Error! Failed to get request token')
        verifier = input('Visit %s and enter code here:' % redirect_url)
        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            logging.error('Error! Failed to get access token')
        logging.debug('received access tokens, writing to config')
        config.set('twitter', 'access_token', auth.access_token)
        config.set('twitter', 'access_token_secret', auth.access_token_secret)

    def main(self):
        '''Main of the TweetPost class'''
        consumer_key = self.config.get('twitter', 'consumer_key')
        consumer_secret = self.config.get('twitter', 'consumer_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        try:
            access_token = self.config.get('twitter', 'access_token')
            access_token_secret = self.config.get('twitter', 'access_token_secret')
            auth.set_access_token(access_token, access_token_secret)
        except NoOptionError as e:
            logging.exception('wtf: %s', e)
            TweetPost.oauth_init(self.config, auth)
        api = tweepy.API(auth)
        try:
            api.update_status(self.tweet)
        except(tweepy.error.TweepError) as e:
            logging.warning("Error occurred while updating status: %s", e)
        else:
            return True

