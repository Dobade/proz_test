# coding=utf-8
import MySQLdb
class MysqlOperate:
    def __init__(self):

    # 指定mysql数据库信息
        self.__coon = MySQLdb.connect('127.0.0.1',"root","","lijianjun",charset="utf8")
    
    def execute_db(self,types,chanel,data=''):
        self.__cur=self.__coon.cursor()
        
        if types=='select':
            sql="select * from weibo_information where chanel='%s'"%chanel
            self.__cur.execute(sql)
            datas=self.__cur.fetchall()
            return datas
        elif types=='insert':
           # data=data.encode('utf-8').split(',')
            sql="insert into weibo_information(chanel,comment) values('%s','%s')"%(chanel,data)
            
            try:
                self.__cur.execute(sql)
                
                self.__coon.commit()

            except:
                self.__coon.rollback()
                
        else:
            pass


    
 
 


