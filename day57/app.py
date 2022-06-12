import pymysql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')

    username = request.form.get('user')
    password = request.form.get('password')
    mobile = request.form.get('mobile')

    print(username, password, mobile)

    # 1. 连接数据库
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='12345678',
                           charset='utf8',
                           db='unicom',
                           )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2. 发送指令
    sql = 'insert into admin(username, password, mobile) values (%s, %s, %s)'
    cursor.execute(sql, [username, password, mobile])
    conn.commit()

    # 3. 关闭连接
    cursor.close()
    conn.close()

    return redirect('/')


@app.route('/user/list')
def user_list():
    # 1. 连接数据库
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='12345678',
                           charset='utf8',
                           db='unicom',
                           )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2. 发送指令
    sql = 'select * from admin'
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 3. 关闭连接
    cursor.close()
    conn.close()

    print(data_list)
    return render_template('user_list.html', data_list=data_list)


if __name__ == '__main__':
    app.run()
