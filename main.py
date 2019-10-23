# -*- coding: utf-8 -*-
""" Fetche e-mail address for a given url into URL_K_FACULTY.

Inputs
------
URL_K_FACULTY : str
    URL string from which e-mail address are extracted.

Outputs
-------
OUTPUT_XLS : str
    Holds extracted emails.

Author
------
Sri Ram Sagar k

Created on Sat Jan 13 15:42:35 2018
"""

from getmails.html_fetcher import URLClerk
from getmails.html_analyzer import HtmlClerk
from getmails.constants import ReObjects
from urllib.error import HTTPError
from itertools import chain

URL_K_FACULTY = "https://xxxxxxx.xxx.xxx/kifaculty/" # Input URL to fetch email addresses.
OUTPUT_XLS = 'k_faculty.xls'

if __name__ == "__main__":
    clerk = URLClerk()                                  # Manager data clerk object.
    html_raw = clerk.get_html(link = URL_K_FACULTY)     # Fetch HTML.

    analyzer = HtmlClerk(html_raw)                      # Manager data to html clerk object. 
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

    # Convert data to pandas data frame and Write to an excel file.
    import pandas as pd
    df = pd.DataFrame(temp_df)
    print(df)
    df.to_excel(OUTPUT_XLS)