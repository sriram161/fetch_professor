# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:42:35 2018

@author: ksrir

@Description: This is the main file to use package getmails.
"""

import re
from getmails.html_fetcher import URLClerk
from getmails.html_analyzer import HtmlClerk
from getmails.constants import ReObjects
from urllib.error import HTTPError

URL_KRASNOW_FACULTY = "https://krasnow.gmu.edu/kifaculty/"

clerk = URLClerk()

html_raw = clerk.get_html(link = URL_KRASNOW_FACULTY)

analyzer = HtmlClerk(html_raw)
lines = analyzer.get_tag('ul')
prof_links = {a.get_text(): a.get('href') for li in lines[-2].find_all('li') for a in li.find_all('a') }

obj = HtmlClerk(clerk.get_html("http://bioengineering.gmu.edu/faculty/agrawal/"))
print(obj(text=re.compile(r".*@gmu.edu")))


for prof,link in prof_links.items():
    try:
        obj = HtmlClerk(clerk.get_html(link))
        emails = [obj(text=re_obj) for re_obj in ReObjects.email_patterns]
        print(emails)
        
    except HTTPError:
        continue
        
        
# =============================================================================
#     print(obj(text = re.compile(r".*@\s*gmu.edu")))
#     print(obj(text = re.compile(r".* AT gmu DOT edu")))
# =============================================================================
