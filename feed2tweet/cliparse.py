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
import os.path
import sys

__version__ = '0.8'

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
        parser.add_argument('-r', '--rss', help='the RSS feed URL to fetch items from',
                            dest='rss_uri', metavar='http://...')
        parser.add_argument('--rss-sections', action='store_true', default=False,
                            dest='rsssections',
                            help='print the available sections of the rss feed to be used in the tweet template')
        self.opts = parser.parse_args()

        if self.opts.cachefile and not os.path.isabs(self.opts.cachefile):
            sys.exit('You should provide an absolute path for the cache file')    

    @property
    def options(self):
        '''return the path to the config file'''
        return self.opts
