# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:36:35 2018

@author: ksrir
"""

import urllib.request

html_handle = urllib.request.urlopen("https://krasnow.gmu.edu/kifaculty/")
print(html_handle.read())