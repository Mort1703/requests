import requests
from bs4 import BeautifulSoup 

url = "https://www.akusherstvo.ru/events/bugaboo/kolyaski-bugaboo/"

requests = requests.get(url)

soup = BeautifulSoup(requests.text , "html.parser")

teme = soup.find_all("div", class_="title")

for temes in teme:
	temes = temes.find("a", {'class':'itemRow'})
	
	if temes is not None:
		print(temes.text)