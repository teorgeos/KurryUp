from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

data1_list = soup.findAll('div', {'class': 'col_inner'})
# pprint(data1)

week_title_list = []
for data1 in data1_list:
    data2 = data1.findAll('a', {'class': 'title'})
    # pprint(data2)
    title_list = []
    title_list = [t.text for t in data2]
    week_title_list.append(title_list)
    
pprint(week_title_list[])