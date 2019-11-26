# coding=utf-8
import redis
from RedisToMysql import MysqlOperate 
import json
from log import logger
pool=redis.ConnectionPool(host='127.0.0.1',password='risk',port=6379,db=1)
r = redis.StrictRedis(connection_pool=pool)
p = r.pubsub()
p.subscribe("lijianjun")
mysql_obj=MysqlOperate()
for item in p.listen():    
    
    if item['type'] == 'message':  
        data =item['data']
        logger.debug("接受到的消息是: %s",data)
       
        mysql_obj.execute_db('insert','lijianjun',data)
        r.set('s',32)
        print data
        if item['data']=='over':
            break;
p.unsubscribe('lijianjun')
print '取消订阅'

