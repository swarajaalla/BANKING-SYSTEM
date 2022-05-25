import mysql.connector
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


class Db_connect:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='Efgeghnlrtq@123')
            self.cursor = self.connection.cursor()
            self.cursor.execute('USE BANK_PROJ')
            print("Database Connected Successfully")
        except:
            print("DataBase not connected")
    
    def display(self,str):
        self.str = str
        self.cursor.execute(str)
        self.records = self.cursor.fetchall()
        table = tabulate(self.records,headers=self.cursor.column_names,
                tablefmt='fancy_grid')
        print(table)
        try:
            df=pd.DataFrame(self.records)
            # print(df[1].dtype)
            if df[1].dtype != object:    
                plt.bar(df[0],df[1])
                plt.show()
        except:
            print("Cannot display")
