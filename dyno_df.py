from datetime import datetime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from urllib.request import Request
import pandas as pd

url = "https://www.hdfcsec.com/market/equity"
req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
page = ureq(req).read()
#page.close()
for loop in range(15):
	date = datetime.now().strftime("%Y_%m_%d__%H_%M_%S_%f")
	filename = date+".xlsx"
	page_soup = soup(page,"html.parser")
	container = page_soup.findAll("div",{"class":"marketGridElement"})
	namel=[]
	valuel=[]
	changeVall=[]
	changePercentVall=[]
	for i in container:
		name = i.findAll("span",{"class":"companyName"})[0].text
		value = i.findAll("span",{"class":"ltpVal"})[0].text
		changeVal = i.findAll("span",{"class":"changeVal"})[0].text
		changePercentVal = i.findAll("span",{"class":"changePercentVal"})[0].text
		namel.append(name)
		valuel.append(value)
		changeVall.append(changeVal)
		changePercentVall.append(changePercentVal)
	dict = {"companyName":namel,"Value":valuel,"changeValue":changeVall,"changePercentValue":changePercentVall}
	df = pd.DataFrame(dict)
	df.index.name = "index"
	df.to_excel(filename)