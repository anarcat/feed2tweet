# Copyright 2016 Carl Chenet <carl.chenet@ohmytux.com>
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
#!/usr/bin/env python3

# Setup for Feed2tweet
'''Setup for Feed2tweet'''

from setuptools import setup

CLASSIFIERS = [
    'Intended Audience :: End Users/Desktop',
    'Environment :: Console',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.4'
]


setup(
    name='feed2tweet',
    version='0.4',
    license='GNU GPL v3',
    description='Parse rss feed and tweet new posts to Twitter',
    long_description='Parse rss feed and tweet new posts to Twitter',
    author = 'Carl Chenet',
    author_email = 'chaica@ohmytux.com',
    url = 'https://github.com/chaica/feed2tweet',
    classifiers=CLASSIFIERS,
    download_url='https://github.com/chaica/feed2tweet',
    scripts=['feed2tweet'],
    install_requires=['feedparser', 'persistentlist', 'tweepy'],
)
