from django.shortcuts import render
from django.core.paginator import Paginator
from pymongo import MongoClient



# list 함수
def index(request):
    # dict 자료형 생성하기
    data = request.GET.copy()

    # MongoClient 객체 얻기
    str_server = "mongodb://192.168.17.128:27017/"
    # str_server = "mongodb://127.0.0.1:27017/"

    # client = MongoClient(str_server)
    client = MongoClient(str_server)

    # DB 선택하기
    mydb = client.mydb

    # MOVIEBOARD 테이블 얻기
    result = list(mydb.MOVIEBOARD.find({}))
    data['page_obj'] = result

    return render(request, 'board/listmongo.html', context=data)

# listjob function
def listjob(request):
    # dict 자료형 생성하기
    data = request.GET.copy()

    # MongoClient 객체 얻기
    str_server = "mongodb://192.168.17.128:27017/"
    # str_server = "mongodb://127.0.0.1:27017/"

    # client = MongoClient(str_server)
    client = MongoClient(str_server)

    # DB 선택하기
    db = client['testdb']

    # WORKGOKR 테이블 얻기
    result = list(db['workgokr'].find({}))
    data['page_obj'] = result

    return render(request, 'board/listjob.html', context=data)



#
def listpage(request):
    data = request.GET.copy()

    # MongoClient 객체 얻기
    client = MongoClient("mongodb://127.0.0.1:27017/")

    # db 선택하기
    db = client.mydb

    # 테이블 내용 얻기
    content = list(db.MOVIEBOARD.find({}))

    # 페이지 개수 설정하기
    paginator = Paginator(content, 10)

    # 데이터 얻기
    page_number = request.GET.get('page', 1)
    data['page_obj'] = paginator.get_page(page_number)

    return render(request, 'board/listpage.html', context=data)
