import pymysql
from flask import current_app
from impala.dbapi import connect
import time, re


def select_t(sql, db_n):
    sql_db = current_app.config['SQL_DB']
    db = pymysql.connect(sql_db[0], sql_db[1], sql_db[2], db_n)
    cursor = db.cursor()
    cursor.execute(sql)
    items = cursor.fetchall()
    return items


def impala_s(sql1):
    # impala_db = current_app.config['IMPALA']
    impala_db = ['192.168.2.123', 21050]
    # impala_db = ['zhuboo.cn', 12123]
    start = time.time()
    conn = connect(host=impala_db[0], port=impala_db[1], database='job_db')
    cursor = conn.cursor()

    cursor.execute('explain %s' % sql1)

    mem = int(re.match('.*Memory=([0-9]+)\..*', cursor.fetchall()[0][0]).group(1)) + 30

    cursor.execute('set mem_limit=' + str(mem) + 'MB;')

    cursor.execute(sql1)
    end = time.time()
    results = cursor.fetchall()
    time0 = end - start

    return results, time0


def result_l(results, x, y):
    x.insert(0, 'product')
    field1 = x
    field2 = y

    list_l = []

    for i in range(len(field2)):
        list_l.append([field2[i]])
        for j in range(len(field1) - 1):
            list_l[i].append(0)

    for i in field2:
        for j in results:
            if i in j:
                index = field1.index(j[0])
                list_l[field2.index(i)][index] = j[2]
    list_l.insert(0, field1)
    return list_l


def result_3d(results, x, y):
    results_l = []
    for row in results:
        results_l.append([x.index(row[0]), y.index(row[1]), int(row[2])])
    return results_l
