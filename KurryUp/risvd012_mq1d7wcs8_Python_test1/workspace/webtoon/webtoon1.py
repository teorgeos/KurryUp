from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

data1 = soup.findAll('a', {'class':'title'})
#pprint(data1)
week_title_list = [t.text for t i ndat]