# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:42:35 2018

@author: ksrir

@Description: This is the main file to use package getmails.
"""

from getmails.html_fetcher import URLClerk
from getmails.html_analyzer import HtmlClerk
from getmails.constants import ReObjects
from urllib.error import HTTPError
from itertools import chain

URL_KRASNOW_FACULTY = "https://krasnow.gmu.edu/kifaculty/"

clerk = URLClerk()

html_raw = clerk.get_html(link = URL_KRASNOW_FACULTY)

analyzer = HtmlClerk(html_raw)
lines = analyzer.get_tag('ul')
prof_links = {a.get_text(): a.get('href') for li in lines[-2].find_all('li') for a in li.find_all('a') }
temp_df = []
for prof,link in prof_links.items():
    try:
        frame = []
        obj = HtmlClerk(clerk.get_html(link))
        emails = [obj(text=re_obj) for re_obj in ReObjects.email_patterns]
        phones = [obj(text=re_obj) for re_obj in ReObjects.phone_patterns]
        frame.append(prof)
        frame.extend(list(chain.from_iterable(emails)))
        frame.extend(list(chain.from_iterable(phones)))
        temp_df.append(frame)
        
    except HTTPError:
        continue
    
  
# Convert data to pandas data frame and Write to an excel file using pandas
import pandas as pd
df = pd.DataFrame(temp_df)
print(df)
df.to_excel('krasnow_faculty.xls')

        
        
