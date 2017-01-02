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
                # tweet option
                confoption = 'tweet'
                if config.has_option(section, confoption):
                    self.tweetformat = config.get(section, confoption)
                else:
                    sys.exit('You should define a format for your tweet with the keyword "tweet" in the [rss] section')

                # pattern format option
                options['patterns'] = {}
                options['patternscasesensitive'] = {}
                for pattern in ['summary_detail', 'published_parsed', 'guidislink', 'authors', 'links', 'title_detail', 'author', 'author_detail', 'comments', 'published', 'summary', 'tags', 'title', 'link', 'id']:
                    currentoption = '{}_pattern'.format(pattern)
                    if config.has_option(section, currentoption):
                        tmppattern = config.get(section, currentoption)
                        if self.stringsep in tmppattern:
                            options['patterns'][currentoption] = [i for i in tmppattern.split(self.stringsep) if i]
                        else:
                            options['patterns'][currentoption] = [tmppattern]

                    # pattern_case_sensitive format
                    currentoption = '{}_pattern_case_sensitive'.format(pattern)
                    if config.has_option(section, currentoption):
                        try:
                            options['patternscasesensitive'][currentoption] = config.getboolean(section, currentoption)
                        except ValueError as _:
                            options['patternscasesensitive'][currentoption] = True

                # check if options['patterns'] always has a counterpart to True in options['patternscasesensitive']
                for patternoption in options['patterns']:
                    if patternoption not in options['patternscasesensitive']:
                        options['patternscasesensitive']['{pattern}_case_sensitive'.format(pattern=patternoption)] = True

                # rsslist
                feeds = []
                currentoption = 'uri_list'
                if config.has_option(section, currentoption):
                    rssfile = config.get(section, currentoption)
                    rsslist = open(rssfile, 'r').readlines()
                    rsslist =  (i.strip() for i in rsslist if i)
                    for rss in rsslist:
                        feeds.append(feedparser.parse(rss))

                # uri
                if not feeds and not self.clioptions.rss_uri:
                    confoption = 'uri'
                    if config.has_option(section, confoption):
                        options['rss_uri'] = config.get('rss', 'uri')
                    else:
                        sys.exit('{confoption} parameter in the [{section}] section of the configuration file is mandatory. Exiting.'.format(section=section, confoptionn=confoption))
                else:
                    options['rss_uri'] = self.clioptions.rss_uri
                # get the rss feed for rss parameter of [rss] section
                feed = feedparser.parse(options['rss_uri'])

            # cache section
            section = 'cache'
            if not self.clioptions.cachefile:
                confoption = 'cachefile'
                if config.has_section(section):
                    options['cachefile'] = config.get(section, confoption)
                else:
                    sys.exit('You should provide a {confoption} parameter in the [{section}] section'.format(section=section, confoption=confoption))
                if not os.path.isabs(options['cachefile']):
                    sys.exit('You should provide an absolute path to the cache file in the [{section}] section'.format(section=section))
            else:
                options['cachefile'] = self.clioptions.cachefile

            # hashtaglist section
            section = 'hashtaglist'
            if not self.clioptions.hashtaglist:
                confoption = 'several_words_hashtags_list'
                if config.has_section(section):
                    options['hashtaglist'] = config.get(section, confoption)
                else:
                    options['hashtaglist'] = False

            # plugins section
            plugins = {}
            section = 'influxdb'
            if config.has_section(section):
                plugins[section] = {}
                for currentoption in ['host','port','user','pass','database']:
                    if config.has_option(section, currentoption):
                        plugins[section][currentoption] = config.get(section, currentoption)
                if 'host' not in plugins[section]:
                    plugins[section]['host'] = '127.0.0.1'
                if 'port' not in plugins[section]:
                    plugins[section]['port'] = 8086
                if 'measurement' not in plugins[section]:
                    plugins[section]['measurement'] = 'tweets'
                for field in ['user','pass','database']:
                    if field not in plugins[section]:
                        sys.exit('Parsing error for {field} in the [{section}] section: {field} is not defined'.format(field=field, section=section))

            # storing results of the parsing
            if feeds:
                self.confs.append((options, config, self.tweetformat, feeds, plugins))
            else:
                self.confs.append((options, config, self.tweetformat, [feed], plugins))
        
    @property
    def confvalues(self):
        '''Return the values of the different configuration files'''
        return self.confs
