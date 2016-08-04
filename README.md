#DB Analysis

##Multivalue DBMS

###sciDB
 
 - 매우 큰 DB에 대한 과학적인 분석을 위하여 개발된 오픈소스 데이터 관리 시스템으로 다차원 배열 지원
 - 기존의 DB와는 다르게 모든 트랜젝션을 지원하고 스키마가 없다.
 - 분석 중심으로 구축되어 storage는 단일 행의 삽입보다는 대량의 자료 로드, 읽기, 쓰기가 가능하다 (병렬처리)
 - 코어는 C++이지만, util은 R, Python을 이용하여 프로그래밍
 - Data Type : int8, int16, int32, int64, unit8 ~ 64, datetime, datetimez, float, double, bool, char, string
 - PostgreSQL는 sciDB의 필수 의존성으로, 메타 데이터 카탈로그에 대한 지원
 
 
[http://m.blog.naver.com/estern/220643329680]

[http://db-engines.com/en/system/SciDB]

[http://www.paradigm4.com/]

API : [http://scidb-py.readthedocs.io/en/stable/classes.html#scidb-array-class]


##Key Value Store

###Redis

 - In-memory 자료구조 DataBase로 캐시와 메시지 브로커로 주로 사용된다.
 - Redis 설치 : http://egloos.zum.com/sweeper/v/3157496
 - Key/Value Store 형식이고, PUT/GET Operation 지원
 - 모두 메모리에 저장되므로 빠른 write/read 속도를 지원한다
 
 - 지원 데이터 타입 : String, Set(String 집합), Sorted Set(score 가중치), Hashes, List
 - RDB (메모리 -> Dist) / AOF (Log file) 방식이 있는데, 두가지 모두 혼용해서 하는것이 좋음! 

![img](http://cfile1.uf.tistory.com/image/202A37504FFBDA60262DD2)

DB 요약 : [http://db-engines.com/en/system/Redis]

API : [http://redis.io/commands]

##Time Sharing DataBase

###InfluxDB (V0.13)

 - Data Type : Int, Float, Boolean, String, Multiple Type 지원
 - HW 사양에 따라서 초당 data input 수, 처리할수있는 column수가 결정됨
 - ; 을 안찍어도 실행이 되는것 이외에는 MySQL Query문이랑 큰 차이가 없음
 - 기본 사용 포트 : 8083, 8086, 8088

InfluxDB 간략 정리 : [http://db-engines.com/en/system/InfluxDB]

InfluxDB 공식 Doc : [https://docs.influxdata.com/]


###Grapana 연동

 Grapana는 데이터를 Graph, Table 등 보기 쉽게 시각적으로 표현해주는 툴입니다. InfluxDB에서 시간 정보와 저장된
 데이터를 간단하게 Graph로 나타내기 위해 이 툴을 사용하였습니다. 설치 방법은 아래와 같습니다.

 - `$ influx` 로 influxDB 접속

 - `CREATE DATABASE grafana` 로 설정정보 저장용 DB 생성

 - Graphana 설치
~~~~
    wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.6.0_amd64.deb
    sudo apt-get install -y adduser libfontconfig
    sudo dpkg -i grafana_2.6.0_amd64.deb
    sudo service grafana-server start
~~~~

 - http://loaclhost:3000 으로 접속, ( ID/PW : admin/admin )

 - Data Sources -> Add new를 하여서 InfluxDB 0.9x와 연동
![addnew](http://cfile30.uf.tistory.com/image/261EA347571438922BE5C1)

 - Dashboard에 New를 클릭하여 Add row -> Add Panel -> Graph를 선택
![newGraph](http://cfile1.uf.tistory.com/image/212721485714416319E0AD)

 - Metrics에서 Qurey를 제어하여 원하는 그래프가 나오도록 조작 및 설정!!
![final](http://cfile23.uf.tistory.com/image/2102784F5714478E0E969B)


API : [http://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdbclient]

[http://hamait.tistory.com/537]

[http://docs.grafana.org/datasources/influxdb/]
