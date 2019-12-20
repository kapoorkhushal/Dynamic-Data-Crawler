from datetime import datetime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from urllib.request import Request

url = "https://www.hdfcsec.com/market/equity"
req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
page = ureq(req).read()
#page.close()
for loop in range(15):
	date = datetime.now().strftime("%Y_%m_%d__%H_%M_%S_%f")
	filename = date+".csv"
	f = open(filename,"w")
	headers = "companyName,Value,changeValue,changePercentValue \n"
	f.write(headers)
	page_soup = soup(page,"html.parser")
	container = page_soup.findAll("div",{"class":"marketGridElement"})
	for i in container:
		name = i.findAll("span",{"class":"companyName"})[0].text
		value = i.findAll("span",{"class":"ltpVal"})[0].text
		changeVal = i.findAll("span",{"class":"changeVal"})[0].text
		changePercentVal = i.findAll("span",{"class":"changePercentVal"})[0].text
		print(name+"\t"+value.strip()+"\t"+changeVal.strip()+"\t"+changePercentVal.strip()+"\n")
		f.write(name+","+value.replace(",","").strip()+","+changeVal.strip()+","+changePercentVal.strip()+"\n")