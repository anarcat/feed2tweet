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

# Add as many tags as possible depending on the tweet length
'''Add as many tags as possible depending on the tweet length'''

# standard library imports
from operator import itemgetter

class AddTags(object):
    '''Add as many tags as possible depending on the tweet length'''
    def __init__(self, tweet, tags):
        '''Constructor of AddTags class'''
        self.tags = tags
        self.tweet = tweet
        self.main()

    def main(self):
        '''Main of the AddTags class class'''
        maxlength = 140
        shortenedlinklength = 23
        linkslength = 0
        linksnb = 0
        tweetlength = len(self.tweet)

        # sort list of tags, the ones with the greater length first
        tagswithindices = ({'text':i, 'length':len(i)} for i in self.tags)
        sortedtagswithindices = sorted(tagswithindices, key=itemgetter('length'), reverse=True)
        self.tags = (i['text'] for i in sortedtagswithindices)

        # count the links
        for element in self.tweet.split():
            if element != ' ' and (element.startswith('http://') or element.startswith('https://')):
                if len(element) > shortenedlinklength:
                    linkslength += len(element)
                    linksnb += 1

        # length of the tweet with shortened links
        shortenedtweetlength = tweetlength - linkslength + (linksnb * shortenedlinklength)
        # add tags is space is available
        for tag in self.tags:
            taglength = len(tag)
            if (shortenedtweetlength + (taglength +1)) <= maxlength:
                self.tweet = ' '.join([self.tweet, tag])
                shortenedtweetlength += (taglength + 1)

    @property
    def finaltweet(self):
        '''return the final tweet with as many tags as possible'''
        return self.tweet
