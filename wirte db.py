import pymysql
# 172.40.75.250 超
# 172.40.75.249 强
db=pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="stu",charset="utf8")
cur = db.cursor()
# try:
sql="insert into sanguo values (14,'张宝','m','蜀国',255,60);"
cur.execute(sql)
db.commit()
# except Exception :
#     db.rollback()



cur.close()
db.close()















