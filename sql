Traceback (most recent call last):
  File "/home/tarena/month02/数据库模块操作/wirte db.py", line 9, in <module>
    cur.execute(sql)
  File "/usr/local/lib/python3.6/dist-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/usr/local/lib/python3.6/dist-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/usr/local/lib/python3.6/dist-packages/pymysql/connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/usr/local/lib/python3.6/dist-packages/pymysql/connections.py", line 732, in _read_query_result
    result.read()
  File "/usr/local/lib/python3.6/dist-packages/pymysql/connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "/usr/local/lib/python3.6/dist-packages/pymysql/connections.py", line 684, in _read_packet
    packet.check_error()
  File "/usr/local/lib/python3.6/dist-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/usr/local/lib/python3.6/dist-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.IntegrityError: (1062, "Duplicate entry '12' for key 'PRIMARY'")


create table dict01 (id int primary key auto_increment,"word" varchar(30) not null,"explain" varchar(127));













