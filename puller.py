#coding:utf-8
import requests
import sqlite3
from datetime import datetime

DATABASE_DIR = "/home/jovyan/work/scrapers/database/"

class Puller(object):
   
    def __init__(self,END_POINT,REQUEST):
        self.END_POINT = END_POINT
        self.REQUEST = REQUEST
        self.URL = self._makeURL()

    def _makeURL(self):
        return self.END_POINT + self.REQUEST

    def pullData(self,content="json"):        
        if content=="json":
            r = requests.get(self.URL)
            return r.json() 

    def sendToSQL(self,dbname,sql): 
        db = DATABASE_DIR + dbname
        with sqlite3.connect(db) as con:
            con.execute(sql)
        return 




class PullRate(Puller):

    def __init__(self):
        END_POINT = "https://bitflyer.jp"
        REQUEST = "/api/echo/price"
        self.dbname = "bitcoin.db"
        super().__init__(END_POINT, REQUEST)
        
    def json(self):
        return super().pullData(content="json")

    def createTableSQL(self):
        dbname = "bitcoin.db"
        db = DATABASE_DIR + dbname
        with sqlite3.connect(db) as con:
            sql = """
                create table bitflyer (
                datetime varchar,
                mid float,
                ask float,
                bid float
            );
            """
        con.execute(sql)

    def sendToSQL(self):
        dbname = "bitcoin.db"
        strnow = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        dic = self.json()
        sql = "INSERT INTO bitflyer values ('{}','{}','{}','{}')".format(strnow,dic["mid"],dic["ask"],dic["bid"])
        super().sendToSQL(dbname=dbname, sql=sql)
        return 



