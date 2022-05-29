import requests
from bs4 import BeautifulSoup 

url = "https://www.akusherstvo.ru/events/bugaboo/kolyaski-bugaboo/"

requests = requests.get(url)
# print(requests.text)

soup = BeautifulSoup(requests.text , "html.parser")
# print(soup, "line 9 is" )
teme = soup.find_all("div", class_="itemInfo")
print(teme, "line 11 is")
test= teme.find_all("p", class_="itemName")
for href  in test.find_all("a" ):
	print (href, "line 14 is")
	# for href_lv1 in 

# print(test, "line 11 is")
for temes in teme:
	temes = temes.find("a", {'class':'itemRow'})
	# print (temes,"line 14 is")
	if temes is not None:
		print(temes.text)