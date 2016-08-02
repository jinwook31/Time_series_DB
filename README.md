#DB Analysis

##Key Value Store

###Redis

 - In-memory 자료구조 DataBase로 캐시와 메시지 브로커로 주로 사용된다.
 - Redis 설치 : http://egloos.zum.com/sweeper/v/3157496
 - Key/Value Store 형식이고, PUT/GET Operation 지원
 - 모두 메모리에 저장되므로 빠른 write/read 속도를 지원한다
 
 - 지원 데이터 타입 : String, Set(String 집합), Sorted Set(score 가중치), Hashes, List
 - RDB (메모리 -> Dist) / AOF (Log file) 방식이 있는데, 두가지 모두 혼용해서 하는것이 좋음! 


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


[http://hamait.tistory.com/537]

[http://docs.grafana.org/datasources/influxdb/]
