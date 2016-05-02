# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
# Copyright © 2016 Carl Chenet <carl.chenet@ohmytux.com>
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


import os.path
import shelve

class PersistentList(object):

    def __init__(self, dbpath, maxitems):
        self.dblist = []
        self.maxitems = maxitems
        if not os.path.exists('.'.join([dbpath, 'db'])):
            self.db = shelve.open(dbpath, writeback=True)
            self.db['idlist'] = []
        else:
            self.db = shelve.open(dbpath, writeback=True) 

    def __str__(self):
        return self.db['idlist'].__repr__()

    def __iter__(self):
        for elem in self.db['idlist']:
            yield elem

    def add(self, id):
        if len(self.db['idlist']) == self.maxitems:
            del self.db['idlist'][0]
        self.db['idlist'].append(id)

    def close(self):
        self.db.close()
        
