import pymysql
# 172.40.75.250 超
# 172.40.75.249 强
p=input("请输入作者")
db=pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="books",charset="utf8")
cur = db.cursor()
sql="select name,author,press,price from book where author = %s and price > %s;"
cur.execute(sql,[p,25])
# for i in cur:
#     print(i)
# one_row=cur.fetchone()
# print(one_row)
# many_row=cur.fetchmany(5)
# print(many_row)
# all_row=cur.fetchall()
# print(all_row)







cur.close()
db.close()
















