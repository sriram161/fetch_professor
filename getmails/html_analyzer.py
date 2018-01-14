# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:59:36 2018

@author: ksrir
"""

from bs4 import BeautifulSoup

class HtmlClerk(BeautifulSoup):
    def __init__(self, html_raw):
        super().__init__(html_raw, 'html.parser')
        
    def get_links(self, pattern = None):
        '''To get all links from a html page with word pattern link "gmu.edu" '''
        if pattern:
            return [link.get('href') for link in self.find_all('a') if pattern in link.get('href')]
        return [link.get('href') for link in self.find_all('a')] 
        
    def get_tag(self , tag):
        return(self.find_all(tag))
        