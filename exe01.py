import pymysql
import re
f=open('dict.txt','r+')
db=pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="dict",charset="utf8")
cur=db.cursor()
list01=[]
for line in f:
    l=re.findall(r"(\w)\s+(.*)",line)
    list01.extend(l)

sql = "insert into dict01 (word,`explain`) values (%s,%s);"
cur.executemany(sql,list01)
db.commit()


cur.close()
db.close()


















