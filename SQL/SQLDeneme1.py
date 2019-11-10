import sqlite3 as sql
import os

class DBTool():
    __address = "Noname.db"

    def __init__(self,*args,**kwargs):
        self.db = None
        self.cur = None
        self.columns = None # COLUMNS =["IL_ID","IL_ADI"]
        self.table = None # TABLE="ST_ILLER"
        self.kwargs = kwargs
        self.dbConnect()
        

    def getColumns(self):
        for key,value in self.kwargs.items():
            if key == "COLUMNS":
                self.columns = value

    def getTableName(self):
        for key,value in self.kwargs.items():
            if key == "TABLE":
                self.table = value

    def dbConnect(self):
        self.db = sql.connect(DBTool.__address)
        self.cur = self.db.cursor()
        self.getColumns()
        self.getTableName()
    
    def select(self):
        columns = ','.join(self.columns)
        query = "SELECT {} FROM {}".format(columns,self.table)
        self.cur.execute(query)
        return self.cur.fetchall()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


