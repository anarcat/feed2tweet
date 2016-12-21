# -*- coding: utf-8 -*-
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
# along with this program.  If not, see <http://www.gnu.org/licenses/

# Push values to a influxdb database
'''Push values to a influxdb database'''

# standard libraries imports
import json

# 3rd party libraries imports
from influxdb import InfluxDBClient

class InfluxdbPlugin(object):
    '''InfluxdbPlugin class'''
    def __init__(self, plugininfo, data):
        '''Constructor of the InfluxdbPlugin class'''
        self.plugininfo = plugininfo
        self.data = data
        self.datatoinfluxdb = []
        self.client = InfluxDBClient(self.plugininfo['host'],
                                self.plugininfo['port'],
                                self.plugininfo['user'],
                                self.plugininfo['pass'],
                                self.plugininfo['database'])
        self.main()

    def main(self):
        '''Main of the PiwikModule class'''
        self.datatoinfluxdb.append({'measurement': self.plugininfo['measurement'], 'fields': {'value': self.data}})
        self.client.write_points(self.datatoinfluxdb)
