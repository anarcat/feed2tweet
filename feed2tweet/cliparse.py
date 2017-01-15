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
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# CLI parsing
'''CLI parsing'''

# standard library imports
from argparse import ArgumentParser
import glob
import os.path
import sys

__version__ = '1.0'

class CliParse(object):
    '''CliParse class'''
    def __init__(self):
        '''Constructor for the CliParse class'''
        self.main()

    def main(self):
        '''main of CliParse class'''
        feed2tweetepilog = 'For more information: https://feed2tweet.readhthedocs.org'
        feed2tweetdescription = 'Take rss feed and send it to Twitter' 
        parser = ArgumentParser(prog='feed2tweet',
                                description=feed2tweetdescription,
                                epilog=feed2tweetepilog)
        parser.add_argument('--version', action='version', version=__version__)
        parser.add_argument('-c', '--config',
                            default=os.getenv('XDG_CONFIG_HOME',
                                              '~/.config/feed2tweet.ini'),
                            nargs='+',
                            dest="config",
                            help='Location of config file (default: %(default)s)',
                            metavar='FILE')
        parser.add_argument('-a', '--all', action='store_true', default=False,
                            dest='all',
                            help='tweet all RSS items, regardless of cache')
        parser.add_argument('-l', '--limit', dest='limit', default=10, type=int,
                            help='tweet only LIMIT items (default: %(default)s)')
        parser.add_argument('--cachefile', dest='cachefile',
                            help='location of the cache file (default: %(default)s)')
        parser.add_argument('-n', '--dry-run', dest='dryrun',
                            action='store_true', default=False,
                            help='Do not actually post tweets')
        parser.add_argument('-v', '--verbose', '--info', dest='log_level',
                            action='store_const', const='info', default='warning',
                            help='enable informative (verbose) output, work on log level INFO')
        parser.add_argument('-d', '--debug', dest='log_level',
                            action='store_const', const='debug', default='warning',
                            help='enable debug output, work on log level DEBUG')
        parser.add_argument('--hashtaglist', dest='hashtaglist',
                            help='a list of hashtag to match')
        parser.add_argument('-p', '--populate-cache', action='store_true', default=False,
                            dest='populate',
                            help='populate RSS entries in cache without actually posting them to Twitter')
        parser.add_argument('-i', '--init', action='store_true', default=False,
                            help='interactively reinitialize Twitter Oauth tokens')
        parser.add_argument('-r', '--rss', help='the RSS feed URL to fetch items from',
                            dest='rss_uri', metavar='http://...')
        parser.add_argument('--rss-sections', action='store_true', default=False,
                            dest='rsssections',
                            help='print the available sections of the rss feed to be used in the tweet template')
        self.opts = parser.parse_args()
        # verify if the path to cache file is an absolute path
        if self.opts.cachefile and not os.path.isabs(self.opts.cachefile):
            sys.exit('You should provide an absolute path for the cache file')    
        # verify if the path to cache file is an absolute path
        # get the different config files, from a directory or from a *.ini style
        for element in self.opts.config:
            if element and not os.path.isabs(element):
                sys.exit('You should provide an absolute path for the config file')    
            if os.path.isdir(element):
                #self.opts.configs = [os.path.join(element, i) for i in os.listdir(element) if i.lower().endswith('.ini')]
                self.opts.configs = glob.glob(os.path.join(element, '*.ini'))
            else:
                # trying to glob the path
                self.opts.configs = glob.glob(element)
        # verify if a configuration file is provided
        if not self.opts.configs:
            sys.exit('no configuration file was found at the specified path(s) with the option -c')

    @property
    def options(self):
        '''return the path to the config file'''
        return self.opts
