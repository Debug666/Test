import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root',passwd='123456',db='t_test',charset='utf8')
cursor = conn.cursor()
# print(conn)
# print(cursor)
sql = "select * from authors"
cursor.execute(sql)
# print(cursor.rowcount)
result = cursor.fetchall()
for row in result:
    print(row)