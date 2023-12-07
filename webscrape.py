from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import os

def message():
	url = 'https://www.bjjhq.com/'

	headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
	source=requests.get(url,headers=headers).text
	soup=BeautifulSoup(source,"html.parser")

	apparel_title=soup.find("h1").get_text()
	apparel_price=soup.find_all("em")[1].get_text()
	apparel_description=soup.find_all("p")[0].get_text()
	apparel_points=soup.find("div", {"class": "desclist"}).find_all("li")

	x = "Good Evening, love. Today, we have \n\n"+apparel_title+" going for "+apparel_price+". \n\n Here is a little description: \n\n "+apparel_description+" \n\n Check it out at "+url
	# print(f"So, on today's menu is ~ {apparel_title} ~ selling for a hot {apparel_price}")
	return x

