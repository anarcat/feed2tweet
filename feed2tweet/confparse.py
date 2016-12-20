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
    def __init__(self, clioptions):
        '''Constructor of the ConfParse class'''
        self.clioptions = clioptions
        self.tweetformat = ''
        self.stringsep = ','
        self.confs = []
        self.main()

    def main(self):
        '''Main of the ConfParse class'''
        for pathtoconfig in self.clioptions.configs:
            options = {}
            # read the configuration file
            config = SafeConfigParser()
            if not config.read(os.path.expanduser(pathtoconfig)):
                sys.exit('Could not read config file')

            # get the format of the tweet
            section = 'rss'
            if config.has_section(section):
                confoption = 'tweet'
                if config.has_option(section, confoption):
                    self.tweetformat = config.get(section, confoption)
                else:
                    sys.exit('You should define a format for your tweet with the keyword "tweet" in the [rss] section')

                # pattern format
                options['patterns'] = {}
                options['patternscasesensitive'] = {}
                for pattern in ['summary_detail', 'published_parsed', 'guidislink', 'authors', 'links', 'title_detail', 'author', 'author_detail', 'comments', 'published', 'summary', 'tags', 'title', 'link', 'id']:
                    currentoption = '{}_pattern'.format(pattern)
                    if config.has_option(section, currentoption):
                        tmppattern = config.get(section, currentoption)
                        if self.stringsep in tmppattern:
                            options['patterns'][currentoption] = [i for i in tmppattern.split(self.stringsep) if i]
                        else:
                            options['patterns'][currentoption] = tmppattern

                    # pattern_case_sensitive format
                    currentoption = '{}_pattern_case_sensitive'.format(pattern)
                    if config.has_option(section, currentoption):
                        options['patternscasesensitive'][currentoption] = config.getboolean(section, currentoption)

            if not self.clioptions.cachefile:
                try:
                    options['cachefile'] = config.get('cache', 'cachefile')
                except (NoOptionError, NoSectionError):
                    sys.exit('You should provide an absolute path to the cache file in the [cache] section')
                finally:
                    if not os.path.isabs(options['cachefile']):
                        sys.exit('You should provide an absolute path to the cache file in the [cache] section')
            else:
                options['cachefile'] = self.clioptions.cachefile

            if not self.clioptions.rss_uri:
                try:
                    options['rss_uri'] = config.get('rss', 'uri')
                except (NoOptionError, NoSectionError):
                    sys.exit('uri parameter in the [rss] section of the configuration file is mandatory. Exiting.')
            else:
                options['rss_uri'] = self.clioptions.rss_uri
            feed = feedparser.parse(options['rss_uri'])

            if not self.clioptions.hashtaglist:
                try:
                    options['hashtaglist'] = config.get('hashtaglist', 'several_words_hashtags_list')
                except (NoOptionError, NoSectionError):
                    options['hashtaglist'] = False
            self.confs.append((options, config, self.tweetformat, feed))

    @property
    def confvalues(self):
        return self.confs
