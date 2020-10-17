# 모듈 불러오기
from django.shortcuts import render
import folium



def index(request):
    # 위도 경도 좌표
    lat_long = [35.3369, 127.7306 ]

    # folium 객체 생성하기
    map = folium.Map(lat_long, zoom_start = 10)

    # 마커 객체 생성하기
    poptext = folium.Html('<b>Jirisan</b><br>' + str(lat_long), script=True)
    popupobj = folium.Popup(poptext, max_width=2650)
    folium.RegularPolygonMarker(location=lat_long, popup=popupobj).add_to(map)

    # context 데이터 설정하기
    txtdata = map._repr_html_()
    contextdata = {'mountain_map':txtdata}

    # 출력하기
    return render(request, 'map/index.html', context=contextdata)
