import pymysql
# 172.40.75.250 超
# 172.40.75.249 强
db=pymysql.connect(host="172.40.75.250",port=3306,user="root",password="123456",database="stu",charset="utf8")
cur = db.cursor()







cur.close()
db.close()














