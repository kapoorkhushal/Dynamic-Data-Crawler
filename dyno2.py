from datetime import datetime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from urllib.request import Request
import pandas as pd

url = "https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
page = ureq(req).read()
#page.close()
date = datetime.now().strftime("%Y_%m_%d__%H_%M_%S_%f")
filename = date+".xlsx"
page_soup = soup(page,"html.parser")
#container = page_soup.findAll("div",{"class":"tabular_data_live_analysis"})
#table = container[0].findAll("table")[0]
container = page_soup.findAll("div",{"id":"tabContent"})
print(container[0].prettify())