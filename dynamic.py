from datetime import datetime
import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

url = "https://www.internetlivestats.com/"
uclient = ureq(url)
page = uclient.read()
uclient.close()
page_soup = soup(page,"html.parser")
container = page_soup.findAll("div",{"class":"col-sm-6 col-md-4"})
print(len(container))
time.sleep(15)
for i in container:
	if(i.findAll("div",{"class":"counterdesc"})):
		header=i.findAll("div",{"class":"counterdesc"})
	elif(i.findAll("div",{"class":"counterdescpop"})):
		header=i.findAll("div",{"class":"counterdescpop"})
	else:
		header=i.findAll("div",{"class":"counter"})
	counter = i.findAll("span",{"class":"rts-counter"})
	print(header[0].text)
	print(counter[0].text)
date = datetime.now().strftime("%Y_%m_%d__%H_%M_%S_%f")
filename = date+".xlsx"
#f = open(filename,"w")
print(filename)