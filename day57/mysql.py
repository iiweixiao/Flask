import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="12345678", charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
cursor.execute(sql, ["韩超", "qwe123", "1999999999"])

conn.commit()

cursor.close()
conn.close()
