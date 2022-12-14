from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
tags = ['seoul', 'busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan', 'gyeonggi', 'gangwon', 'chungbuk', 'chungnam', 'jeonnam', 'jeonbuk', 'jeonnam', 'gyeongbuk', 'gyeongnam', 'jeju', 'jeonbuk', 'sejong']

serviceKey = "7TPAcn5Q2SsoTDCvy3aYVULw5LCR0OZouQshO4vHOfMwEvRw1Dms2WtzqLx1z61BIh4HDSunWsnKjSIvwIfb1A%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def check_air(itemCode, location):
    value = []
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst"
    numOfRows = "10"
    pageNo = "1"
    dataGubun = "DAILY"
    searchCondition = "MONTH"
    ver = "1.3"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('itemCode') : itemCode, quote_plus('dataGubun') : dataGubun, quote_plus('searchCondition') : searchCondition , quote_plus('ver') : ver })
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    if location != "all":
        value.append(soup.find(location).text)
    else:
        for tag in tags:
            value.append(soup.find(tag).text)
    return value
