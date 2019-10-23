# -*- coding: utf-8 -*-
""" URLClerk to get data from input link.

Author
------
Sri Ram Sagar K

Created on Sat Jan 13 15:44:15 2018
"""

from urllib.request import urlopen

class URLClerk(object):
    def get_html(self, link):
        return urlopen(link).read()