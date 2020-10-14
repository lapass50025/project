# 프로젝트 요구사항

* 구름에서 동작시키기
* 구름에 MongoDB 올리기
* 페이징 구현하기
* 화면 정의서 작성하기


# 개발 환경 구축하기

* mongo docker 실행시키기
sudo docker start learn_mongo
sudo docker ps -a

* mongo 서버의 IP 주소를 확인한다.
sudo docker inspect learn_mongo | grep IPAddress
IP 주소는 172.17.0.2 이다.

# 구름 설정하기

## 구름에 모듈 설치하기

$ pip install bs4
$ pip install lxml
$ pip install pymongo

## mongod 서버 실행하기
mongod

