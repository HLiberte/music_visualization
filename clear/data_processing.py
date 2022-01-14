import pandas as pd
from sqlalchemy import create_engine
import pymysql

#索引命名
music = pd.read_csv('music_message.csv',encoding='utf-8',header=None)
music.columns = ['id','title','author','date','tag','collection','transmit','comments','songs','play']

#数据清洗
music.isnull().sum()
music.replace('分享','0',inplace=True)
music.replace('评论','0',inplace=True)
del music['Unnamed: 0']

#存储数据库
engine = create_engine('mysql+pymysql://root:root@localhost:3306/music')
music.to_sql('music_clear1',con=engine,index=True,if_exists='replace')
sql_data = "select * from music_clear1"
df = pd.read_sql_query(sql_data,engine)