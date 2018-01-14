# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:41:11 2018

@author: ksrir
"""
import re

class ReObjects(object):
    ''' Regex precompiled objects based on pattern'''
    emails = (r".*@\s*gmu\s*.\s*edu", r".*AT\s*(gmu|GMU)\s*DOT\s*(edu|EDU)")
    phones = (r"(\d{3})\s*-\s*\d{3}\s*-\s*\d{4}",)
    
    email_patterns = [re.compile(obj) for obj in emails]
    phone_patterns = [re.compile(obj) for obj in phones]
    