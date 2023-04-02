import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.bnn.in.th/th/p/smartphone-and-accessories/smartphone/samsung-smartphone'
data = requests.get(url)
# print(data)

soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.text)
data = soup.find('div',{'class':'product-list'})
# print(data)
# title ('div',{'class':'product-name'})
# price ('div',{'class':'product-price'})
title_list = []
price_list = []

for p in data:
    title_tag = p.find('div',{'class':'product-name'})
    if title_tag is not None:
        title = title_tag.text.strip()
        title_list.append(title)

    price_tag = p.find('div',{'class':'product-price'})
    if price_tag is not None:
        price = price_tag.text.strip()
        price_list.append(price)


def writecsv(col_data):
    with open('phone.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        for row in col_data:
            fw.writerow(row)
         #datalist = ['pen','pencil','eraser']

writecsv([title_list, price_list])