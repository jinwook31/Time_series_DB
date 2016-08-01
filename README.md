#Time Series DB

###InfluxDB (V0.13)

 - Data Type : Int, Float, Boolean, String, Multiple Type 지원
 - HW 사양에 따라서 초당 data input 수, 처리할수있는 column수가 결정됨
 - 기본 사용 포트 : 8083, 8086, 8088
 
###Grapana 연동

 - '$ influx' 로 influxDB 접속

 - 'CREATE DATABASE grafana' 로 설정정보 저장용 DB 생성

 - Graphana 설치
~~~~
    $ wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.6.0_amd64.deb
    $ sudo apt-get install -y adduser libfontconfig
    $ sudo dpkg -i grafana_2.6.0_amd64.deb
    $ sudo service grafana-server start
~~~~

  - http://loaclhost:3000 으로 접속, ( ID/PW : admin/admin )


[http://db-engines.com/en/system/InfluxDB]

[https://docs.influxdata.com/]

