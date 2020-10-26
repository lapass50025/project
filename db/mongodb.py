# 모듈 불러오기
from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient
import sys
import time

def ConnectDB():
    """
    pymongo 연결하기
    리턴값 : MongoCLient 객체
    """
    # str_server = "mongodb://192.168.219.110:27017/"
    str_server = "mongodb://127.0.0.1:27017/"

    client = MongoClient(str_server)
    return client

def InsertDB( client, dbname, tbname, dataList ):
    """
    MOVIEBOARD 테이블에 데이터를 추가한다.
    client : MongoClient 객체
    dataList : MOVIEBOARD 정보를 담고 있는 리스트 변수 ( NUMBER, ID, NICKNAME, RANK, TITLE, DATE  )
    """
    # DB 선택하기
    db = client[dbname]

    # dict 데이터 객체 생성하기
    data = dict()
    data['NUMBER'] = dataList[0]
    data['ID'] = dataList[1]
    data['NICKNAME'] = dataList[2]
    data['RANK'] = dataList[3]
    data['TITLE'] = dataList[4]
    data['DATE'] = dataList[5]    

    db[tbname].insert(data)

def ShowDB( client, dbname, tbname ):
    """
    MOVIEBOARD 테이블의 내용을 출력한다.
    client : MongoClient 객체
    """

    # DB 선택하기
    db = client[dbname]

    # cursor 얻기
    cursor = db[tbname].find()

    nCount = 1
    for row in cursor:
        print("%d" %nCount)
        print("게시판 번호 : %s" %row['NUMBER'])
        print("아이디 : %s" %row['ID'])
        print("별명 : %s" %row['NICKNAME'])
        print("평점 : %s" %row['RANK'])
        print("감상평 : %s" %row['TITLE'])
        print("작성일 : %s" %row['DATE'])
        print("-"*20)
        nCount = nCount + 1

# 한 페이지 읽기
def ReadPage(client, nPage):
    """
    네이버 평점 페이지를 읽는다.
    client : MongoClient 객체
    nPage : 페이지 번호 (한 페이지당 10개의 글)
    """

    # 헤더 설정하기
    headers = dict()
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

    # 네이버 평점 사이트 GET 메소드 호출하기
    strUrl = "https://movie.naver.com/movie/point/af/list.nhn?&page={}&page=1".format(nPage)
    res = requests.get( strUrl, headers = headers )
    if res.status_code != 200:
        print("HTTP GET 실패 : %d" %(res.status_code) )
        sys.exit()

    # BeautifulSoup 객체 만들기
    strText = res.content.decode( res.encoding )
    soup = BeautifulSoup( strText, 'lxml')
    time.sleep(1)

    elem = soup.find("tbody")
    elemList = elem.find_all("tr")

    for rows in elemList:
        dataList = list()

        cols = rows.find_all("td")
        for i, col in enumerate(cols):
            if i == 0:
                strNumber = col.get_text()
            if i == 1:
                elem = col.find("a")
                strNickName = elem.get_text()

                elem = col.find("span", attrs = {'class':'st_on'})
                strRank = elem['style']
                n = strRank.find(":")
                strRank = strRank[n+1:]

                elem = col.find("br")
                navString = elem.next_sibling
                strTitle = str(navString.string)
                strTitle = strTitle.strip()

            if i == 2:
                elem = col.find('a')
                strDate = col.get_text()
                strDate = strDate[-8:]
                strId = elem.get_text()

        # 데이터베이스에 추가하기
        dataList.append(strNumber)
        dataList.append(strId)
        dataList.append(strNickName)
        dataList.append(strRank)
        dataList.append(strTitle)
        dataList.append(strDate)

        InsertDB(client, 'testdb', 'jobsite', dataList)

# 메인 함수
def main():
    # DB 초기화하기
    client = ConnectDB()

    # 페이지 읽어오기
    for i in range(1, 2):
        ReadPage(client, i)
        print("{} 번째 페이지 읽는 중".format(i))

    # 출력하기
    ShowDB(client, 'testdb', 'jobsite')

    # MongoClient 객체 닫기
    client.close()

# main 함수 호출하기
if __name__ == "__main__":
    main()
