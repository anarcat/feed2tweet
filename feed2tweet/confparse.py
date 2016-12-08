# -*- coding: utf-8 -*-
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
# along with this program.  If not, see <http://www.gnu.org/licenses/

# Get values of the configuration file
'''Get values of the configuration file'''

# standard library imports
from configparser import SafeConfigParser, NoOptionError, NoSectionError
import os
import os.path
import sys

# 3rd party library imports
import feedparser

class ConfParse(object):
    '''ConfParse class'''
    def __init__(self, options):
        '''Constructor of the ConfParse class'''
        self.options = options
        self.tweetformat = ''
        self.main()

    def main(self):
        '''Main of the ConfParse class'''
        # read the configuration file
        config = SafeConfigParser()
        if not config.read(os.path.expanduser(self.options.config)):
            sys.exit('Could not read config file')

        # get the format of the tweet
        if config.has_section('rss'):
            if 'tweet' in config['rss']:
                self.tweetformat = config.get('rss','tweet')
            else:
                sys.exit('You should define a format for your tweet with the keyword "tweet" in the [rss] section')

        if not self.options.cachefile:
            try:
                self.options.cachefile = config.get('cache', 'cachefile')
            except (NoOptionError, NoSectionError):
                sys.exit('You should provide an absolute path to the cache file in the [cache] section')
            finally:
                if not os.path.isabs(self.options.cachefile):
                    sys.exit('You should provide an absolute path to the cache file in the [cache] section')

        if not self.options.rss_uri:
            try:
                self.options.rss_uri = config.get('rss', 'uri')
            except (NoOptionError, NoSectionError):
                sys.exit('uri parameter in the [rss] section of the configuration file is mandatory. Exiting.')
        self.feed = feedparser.parse(self.options.rss_uri)

        if not self.options.hashtaglist:
            try:
                self.options.hashtaglist = config.get('hashtaglist', 'several_words_hashtags_list')
            except (NoOptionError, NoSectionError):
                self.options.hashtaglist = False
        self.config = config

    @property
    def confvalues(self):
        return (self.options, self.config, self.tweetformat, self.feed)
