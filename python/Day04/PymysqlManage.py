# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/28 0028 下午 2:13
@Author  : fengaijun
@File    : MysqlManage.py

'''
import pymysql
def connect_database(database):
    # 连接数据库
    conn = pymysql.connect(
        host="10.145.6.12",
        user="admin",
        password="16#XrC$T39aR",
        database=database
    )
    return conn
#连接指定数据库-创建表
def connect_database_createtable(database,sql):
    #连接数据库
    conn = connect_database(database)
    #获取游标
    cursor = conn.cursor()
    cursor.execute(sql)   
    cursor.execute("show tables")
    for table in cursor:
        print(table)
#批量数据插入
def connect_database_edittable_insert(database,sql,sqlvalues):
    #连接数据库
    conn = connect_database(database)
    print(conn)
    #获取游标
    cursor = conn.cursor()
    cursor.executemany(sql,sqlvalues)

    rowcount = cursor.rowcount
    print(f"第{rowcount}行记录，添加成功！！！")
    conn.commit()
    #查询语句
    cursor = conn.cursor()
    cursor.execute("select * from table_test")
    print(cursor)
    # for x in cursor:
    #     print(repr(x))
    # print("================")
    #获取所有数据
    select_showall("mind_account","select * from table_test")
def connect_createdatabase():
    #连接数据库
    conn = pymysql.connect(
        host = "10.145.6.12",
        user = "admin",
        password = "16#XrC$T39aR",
    )
    print(conn)
    #获取游标
    cursor = conn.cursor()
    sql = "create database MaShangTest"
    cursor.execute(sql)
    cursor.execute("show databases")
    #遍历结果
    for database in cursor:
        print(database)


def select_showall(database,sql):
     """
     查询数据，并返回查询结果
     :param database:
     :param sql:
     :return:
     """
     conn=connect_database(database)
     # 获取游标实例
     cursor = conn.cursor()
     cursor.execute(sql)
     # 查看所有返回结果
     allrows = cursor.fetchall()
     # 返回第一条记录
     onerow=cursor.fetchone()
     # 返回多条记录
     manyrow=cursor.fetchmany(3)
     print(allrows)
     print(type(allrows))

if __name__ == '__main__':
    # sql = "CREATE TABLE table_test ( id int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID', name varchar(255) NOT NULL COMMENT '姓名', age int(11) NOT NULL COMMENT '年龄', email varchar(255) DEFAULT NULL COMMENT '邮箱', PRIMARY KEY (id) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='表格注释';"
    # connect_database_createtable("mind_account",sql)
    # connect_createdatabase()   ---账号无权限创建数据库
    sql1 = "insert into table_test (name,age,email) values (%s,%s,%s);"
    sqlvalues =[('李四01',23,'12131@qq.com'),('李四02',23,'12131@qq.com'),('李四03',23,'12131@qq.com'),('李四04',23,'12131@qq.com'),('李四05',23,'12131@qq.com'),('李四06',23,'12131@qq.com'),('李四07',23,'12131@qq.com'),('李四08',23,'12131@qq.com'),('李四09',23,'12131@qq.com'),('李四10',23,'12131@qq.com')]
    connect_database_edittable_insert("mind_account",sql1,sqlvalues)
    # sql ="select * from table_test"
    # select_showall("mind_account",sql)