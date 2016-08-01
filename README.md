#Time Series DB

###InfluxDB (V0.13)

 - Data Type : Int, Float, Boolean, String, Multiple Type 지원
 - HW 사양에 따라서 초당 data input 수, 처리할수있는 column수가 결정됨
 - 기본 사용 포트 : 8083, 8086, 8088
 

[http://db-engines.com/en/system/InfluxDB]

[https://docs.influxdata.com/]


###Grapana 연동

 - `$ influx` 로 influxDB 접속

 - `CREATE DATABASE grafana` 로 설정정보 저장용 DB 생성

 - Graphana 설치
~~~~
    $ wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.6.0_amd64.deb
    $ sudo apt-get install -y adduser libfontconfig
    $ sudo dpkg -i grafana_2.6.0_amd64.deb
    $ sudo service grafana-server start
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
