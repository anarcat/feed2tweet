#!/usr/bin/env python3
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

# Remove duplicates from the final string before sending the tweet
'''Remove duplicates from the final string before sending the tweet'''

class RemoveDuplicates(object):
    '''Remove duplicates from the final string before sending the tweet'''
    def __init__(self, tweet):
        '''Constructor of RemoveDuplicates class'''
        self.tweet = tweet
        self.main()

    def main(self):
        '''Main of the RemoveDuplicates class'''
        # identify duplicate links
        links = []
        for element in self.tweet.split():
            if element != ' ' and (element.startswith('http://') or element.startswith('https://')):
                newlink = True
                # if we already found this link, increment the counter
                for i,_ in enumerate(links):
                    if links[i]['link'] == element:
                        newlink = False
                        links[i]['count'] += 1
                if newlink:
                    links.append({'link': element, 'count': 1}) 
        # remove duplicates
        validatedlinks = []
        for i in range(len(links)):
            if links[i]['count'] >= 2:
                validatedlinks.append(links[i])
        wildcard = 'FEED2TWEETWILDCARD'
        for element in validatedlinks:
            for i in range(element['count']): 
                # needed for not inversing the order of links if it is a duplicate
                # and the second link is not one
                if i == 0:
                    self.tweet = self.tweet.replace(element['link'], wildcard, 1 )
                else:
                    self.tweet = self.tweet.replace(element['link'], '', 1)
            # finally 
            self.tweet = self.tweet.replace(wildcard, element['link'], 1)
        # remove all 2xspaces
        self.tweet = self.tweet.replace('  ', ' ')

    @property
    def finaltweet(self):
        '''return the final tweet after duplicates were removed'''
        return self.tweet
