import pymysql
f=open('/home/tarena/10086.jpg','rb+')
data=f.read()
db=pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="stu",charset="utf8")
cur=db.cursor()

sql="update person set image=%s where id=1;"
cur.execute(sql,[data])
db.commit()
















