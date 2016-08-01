import argparse
import time
import random
from datetime import datetime
from influxdb import InfluxDBClient


def main(host='localhost', port=8086):
    user = 'root'
    password = 'root'
    dbname = 'example'
    dbuser = 'root'
    dbuser_password =  'root'
    query = 'select * from test' #table

    client = InfluxDBClient(host, port, user, password, dbname)

    #Create
    print("Create database: " + dbname)
    client.create_database(dbname)

    print("Create a retention policy")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("Switch user: " + dbuser)
    client.switch_user(dbuser, dbuser_password)

    print "Update\n"
    #Update
    loop = 0
    while loop < 1000:
	loop = loop + 1
	time.sleep(2);
	        
	print("Write points: {0}".format(get_Json()))
        client.write_points(get_Json())

    print("\nQueying data: " + query)
    result = client.query(query)
    print("Result: {0}".format(result))


    print "\nRetrieve\n"
    #Retrieve
    result = client.query('SELECT * FROM test WHERE BoolVal=true')
    print("Result: {0}".format(result))

    print("Switch user: " + user)
    client.switch_user(user, password)

    #Delete
    print("Drop database: " + dbname)
    #client.drop_database(dbname)


def get_Json():
    i = random.randrange(1,500)
    f = random.random()
    b = random.choice([True, False])

    json_body = [
        {
            "measurement": "test", #table
            "tags": {
                "host": "server01",
                "region": "kor"
            },
	    #"time": str(datetime.now()),
            "fields": {
                "IntVal": i,
                "FloatVal": f,
                "BoolVal": b,
                "StringVal": "text!"
            }
        }
    ]

    return json_body


def parse_args():
    parser = argparse.ArgumentParser(
        description='parameter Test Code')
    parser.add_argument('--host', type=str, required=False, default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
