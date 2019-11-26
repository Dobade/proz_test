# coding=utf-8
import redis
import log
from log import logger
pool=redis.ConnectionPool(host='127.0.0.1',password='risk',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)
while True:
    input = raw_input("publish:")
    r.publish('lijianjun',input)
    logger.debug("发布的消息是：%s", input)
    if input == 'over':
        print '停止发布'
        break;
    

