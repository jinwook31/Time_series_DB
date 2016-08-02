import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

#Create
print "Create Values \n\n"
r.set('String', 'text') #Key, Value
r.set('num',10)

r.lpush('list',1,2,3,4) #list

r.hmset('User', {'name':'root', 'val':25}) #hash


#Retrive
print "Retrive Values \n"
print "Key/Value"
value = r.get('String')
print value + "\n"

print "List"
print r.lrange('list',0,3)

print "\nHash"
print r.hgetall('User')
print r.hget('User','val') + "\n\n"


#Update
print "Update Value\n"
r.incrby('num',25)
print "Change num Value :" + r.get('num')


#Delete
print "\nDelete num Key"

exist = r.exists('num')
if exist:
    print "num exist"
    print "Delete num"
    r.delete('num')

    exist = r.exists('num')
    if not exist:
        print "Delete done"
