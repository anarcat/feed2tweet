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

# Filter an entry of the RSS feeds
'''Filter an entry of the RSS feeds'''

# standard library imports
from configparser import SafeConfigParser, NoOptionError, NoSectionError
import os
import os.path
import sys

# 3rd party library imports
import feedparser

class FilterEntry(object):
    '''FilterEntry class'''
    def __init__(self, elements, entry, options):
        '''Constructor of the FilterEntry class'''
        self.matching = {}
        self.entry = entry
        self.elements = elements
        self.options = options
        self.main()

    def main(self):
        '''Main of the FilterEntry class'''
        for i in self.elements:
            if i not in self.entry:
                sys.exit('The element {} is not available in the RSS feed. The available ones are: {}'.format(i, [j for j in self.entry]))
            if not self.options['patterns']:
                self.matching[i] = self.entry[i]
            else:
                # pattern matching on the title of the RSS feed
                for patternlist in self.options['patterns']:
                    for pattern in self.options['patterns'][patternlist]:
                        if not self.options['patternscasesensitive']['{}_case_sensitive'.format(patternlist)]:
                            # not case sensitive, so we compare the lower case
                            finalpattern = self.options['patterns'][pattern].lower() 
                            finaltitle = self.entry[pattern.split('_')[0]].lower()
                            if finalpattern in finaltitle:
                                self.matching[i] = self.entry[i]
                        else:
                            # case sensitive, so we use the user-defined pattern
                            if pattern in self.entry['title']:
                                self.matching[i] = self.entry[i]

    @property
    def finalentry(self):
        '''Return the processed entry'''
        return self.matching
