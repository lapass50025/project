from django.shortcuts import render
from pymongo import MongoClient



# list 함수
def index(request):
    # dict 자료형 생성하기
    data = request.GET.copy()

    # MongoClient 객체 얻기
    client = MongoClient('mongodb://192.168.219.110:27017/')

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
    client = MongoClient('mongodb://192.168.219.110:27017/')

    # DB 선택하기
    mydb = client.mydb

    # WORKGOKR 테이블 얻기
    result = list(mydb.WORKGOKR.find({}))
    data['page_obj'] = result

    return render(request, 'board/listjob.html', context=data)


