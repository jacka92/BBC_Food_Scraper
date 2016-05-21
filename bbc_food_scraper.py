import requests
from bs4 import BeautifulSoup
url = "http://www.bbc.co.uk/food"
dict = {}

def crawl_bbc_food(url):
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a', href=True):
         href = link['href']
         #print href
         has_link = dict.has_key(href)
         if (href[0:6] == "/food/") & (not(has_link)):
        	print(href)
        	dict[href]=href
        	#save to file
        	crawl_bbc_food("http://bbc.co.uk" + href)

crawl_bbc_food(url)