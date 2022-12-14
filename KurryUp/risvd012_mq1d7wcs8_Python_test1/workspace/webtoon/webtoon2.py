from bs4 import BeautifulSoup
from pprint import pprint
import requests
from urllib.request import urlretrieve

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

data1_list = soup.findAll('div', {'class': 'col_inner'})
# pprint(data_list)

li_list = []
for data1 in data1_list:
    li_list.extend(data1.findAll('li'))
#pprint(li_list)

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    # print(title, img_src)
    urlretrieve(img_src, title+'.jpg')