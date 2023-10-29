# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:54:09 2022

@author: Mitchell
"""

import DotaScraper
import csv


#testing


usa, eu, sea, china = DotaScraper.get_data()

"""html_text = DotaScraper.get_html()

usa = DotaScraper.get_data(html_text[0], 'Americas')
eu = DotaScraper.get_data(html_text[1], 'Europe')
sea = DotaScraper.get_data(html_text[2], 'Southeast Asia')
china = DotaScraper.get_data(html_text[3], 'China')"""

usa.show()
eu.show()
sea.show()
china.show()


