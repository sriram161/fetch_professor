# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:44:15 2018

@author: ksrir
"""

from urllib.request import urlopen

class URLClerk(object):
    def get_html(self, link):
        return urlopen(link).read()