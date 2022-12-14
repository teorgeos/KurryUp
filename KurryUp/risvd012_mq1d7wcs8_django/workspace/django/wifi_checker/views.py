from django.shortcuts import render
from .models import Wifi
import csv


def index(request):
    return render(request, 'wifi_checker/wifi_main.html', context)


def detail(request, location):
    wifiList = Wifi.objects.filter(instlSignguNm=location)
    context = {'location': location, 'centerLat': wifiList[0].latitude, 'centerLon': wifiList[0].longitude, 'wifiList': wifiList}
    return render(request, 'wifi_checker/wifi_main.html', context)


def bulk_import(request):
    CSV_PATH = 'static/wifi_list.csv'

    with open(CSV_PATH, newline='', encoding='euc-kr') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Wifi.objects.create(
                instlCtprvnNm=row['설치시도명'],
                instlSignguNm=row['소재지도로명주소'].split(' ')[1],
                instlNm=row['설치장소명'],
                instlLcDesc=row['설치장소상세'],
                svcProvdNm=row['서비스제공사명'],
                latitude=row['위도'],
                longitude=row['경도'],
            )
    return