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

"""Checks an RSS feed and posts new entries to twitter."""

# standard libraires imports
import codecs
import logging
import os
import sys

# 3rd party libraries imports
import feedparser
from persistentlist import PersistentList
import tweepy

# app libraries imports
from feed2tweet.cliparse import CliParse
from feed2tweet.confparse import ConfParse
from feed2tweet.removeduplicates import RemoveDuplicates
from feed2tweet.tweetpost import TweetPost

class Main(object):
    '''Main class of Feed2tweet'''

    def __init__(self):
        self.main()

    def main(self):
        """The main function."""
        clip = CliParse()
        options = clip.options
        logging.basicConfig(level=options.log_level.upper(), format='%(message)s')
        cfgp = ConfParse(options)
        options, config, tweetformat, feed = cfgp.confvalues

        cache = PersistentList(options.cachefile[0:-3], 100)
        if options.hashtaglist:
            severalwordshashtags = codecs.open(options.hashtaglist,
                                               encoding='utf-8').readlines()
            severalwordshashtags = [i.rstrip('\n') for i in severalwordshashtags]
        # fixing rss2twitter most old bug
        # reverse feed entries because most recent one should be sent as the last one in Twitter
        entries = feed['entries'][0:options.limit]
        entries.reverse()
        totweet = []
        if not options.all:
            for i in entries:
                if i['id'] not in cache:
                    totweet.append(i)
        else:
            totweet = entries

        for entry in totweet:
            logging.debug('found feed entry %s, %s', entry['id'], entry['title'])

            rss = {
                'id': entry['id'],
            }

            severalwordsinhashtag = False
            # lets see if the rss feed has hashtag
            if 'tags' in entry:
                hastags = True
            else:
                hastags = False

            if hastags:
                if options.hashtaglist:
                    prehashtags = entry['tags'][0]['term']
                    tmphashtags = entry['tags'][0]['term']
                    for element in severalwordshashtags:
                        if element in prehashtags:
                            severalwordsinhashtag = True
                            tmphashtags = prehashtags.replace(element,
                                                              ''.join(element.split()))
                if severalwordsinhashtag:
                    # remove ' from hashtag
                    tmphashtags = tmphashtags.replace("'", "")
                    # remove - from hashtag
                    tmphashtags = tmphashtags.replace("-", "")
                    # remove . from hashtag
                    tmphashtags = tmphashtags.replace(".", "")
                    finalhashtags = tmphashtags.split(' ')
                    # issue with splitting hashtags in 2 words is right there
                    rss['hashtag'] = ' '.join(['#%s' % i for i in finalhashtags])
                else:
                    rss['hashtag'] = ' '.join(['#%s' % i for i in entry['tags'][0]['term'].split()[:2]])

            elements=[]
            for i in tweetformat.split(' '):
                tmpelement = ''
                # if i is not an empty string
                if i:
                    if i.startswith('{') and i.endswith('}'):
                        tmpelement = i.strip('{}')
                        elements.append(tmpelement)

            # match elements of the tweet format string with available element in the RSS feed
            matching = {}
            for i in elements:
                if i not in entry:
                    sys.exit('The element {} is not available in the RSS feed. The available ones are: {}'.format(i, [j for j in entry]))
                matching[i] = entry[i] 
            tweetwithnotag = tweetformat.format(**matching)
            # only append hashtags if they exist
            if 'hashtag' in rss:
                finaltweet = ' '.join([tweetwithnotag, rss['hashtag']])
            else:
                finaltweet = tweetwithnotag
            # remove duplicates from the final tweet
            dedup = RemoveDuplicates(finaltweet)
            finaltweet = dedup.finaltweet

            if options.dryrun:
                logging.warning(finaltweet)
            else:
                TweetPost(config, finaltweet)

                # We keep the first feed in the cache, to use feed2tweet
                # in normal mode the next time
                cache.add(rss['id'])
        # do not forget to close cache (shelf object)
        cache.close()
