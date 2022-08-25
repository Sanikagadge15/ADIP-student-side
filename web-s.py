import threading
import requests
from bs4 import BeautifulSoup
import csv
import time


import pandas as pd

URL="https://disabilityaffairs.gov.in/content/page/adip.php"
page= requests.get(URL)

soup = BeautifulSoup(page.content,'html5lib')

schemes=[] #List to store name of the product



for row in soup.find('div', attrs={'class':'col-md-9 brief-history'}).findAll('li'):
	scheme={}
	scheme['name']=row.a.text
	scheme['url']=row.a['href']
	schemes.append(scheme)
	print('Appended')	
	
print(schemes)
filename= 'schemes.csv'
with open(filename, 'w',newline='') as f:
	w = csv.DictWriter(f, ['name','url'])
	w.writeheader()
	print('Columns written')
	for scheme in schemes:
		w.writerow(scheme)
	



