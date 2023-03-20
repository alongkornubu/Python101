from bs4 import BeautifulSoup
import requests

url = 'https://www.urbandictionary.com/browse.php?character=A'
web_data = requests.get(url)
print(web_data.text)

soup = BeautifulSoup(web_data.text,'html.parser')
find_class = soup.find('div',{'class':'_tr-widget'})
# print(find_class)






