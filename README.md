#Time Series DB

###InfluxDB (V0.13)

 - Data Type : Int, Float, Boolean, String, Multiple Type 지원
 - HW 사양에 따라서 초당 data input 수, 처리할수있는 column수가 결정됨
 - ; 을 안찍어도 실행이 되는것 이외에는 MySQL Query문에 큰 차이가 없음
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
