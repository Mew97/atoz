import pymysql
import sys

db = pymysql.connect('192.168.11.161', 'root', '123456', 'job_db')

cursor = db.cursor()

# cursor.execute('show tables;')
# a = cursor.fetchall()
# sql = ''
# cursor.execute('select * from city_area;')
# b = cursor.fetchall()
#
# for row in b:
#     for col in row:
#         print(col, end='\t')
#     print('\n')
# print(a)

filename = sys.argv[2]
table_name = sys.argv[1]
with open(filename, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        col = line.split('')
        cursor.execute('insert into %s (city, pcv_name, area_name, avg, count, count_c) value ("%s", "%s", "%s", "%s", "%s", "%s")' % (table_name, col[0], col[1], col[2], col[3], col[4], col[5]))
    db.commit()
    f.close()

# insert into city_area2 (city, pcv_name, area_name, avg, count, count_c) value ("111", "11", "1111", "111", "1111", "1111");

# create table city_area (id int primary key auto_increment,city varchar(50), pcv_name varchar(50), area_name varchar(50), avg varchar(50), count varchar(50), count_c varchar(50)) default charset=utf8;

# create table city_area1 (city varchar(50), pcv_name varchar(50), area_name varchar(50), avg varchar(50), count varchar(50), count_c varchar(50)) default charset=utf8;

# sqoop export --connect jdbc:mysql://192.168.11.161:3306/job_db --username root --password 123456 --table city_area1 --export-dir /user/hive/warehouse/job_db.db/city_info2 --fields-terminated-by '\t'

# create table city_info1 row format delimited fields terminated by '/t' as select * from city_info;

# create table t_sh row format delimited fields terminated by '\t' as select j_t,j_e,avg(salary_range) from big_t where city='北京' group by j_t,j_e;

sqoop export \
--connect "jdbc:mysql://192.168.11.161:3306/job_db?useUnicode=true&characterEncoding=utf-8" \
--username root \
--password 123456 \
--table t_sh \
--export-dir "/user/hive/warehouse/job_db.db/t_sh" \
--input-fields-terminated-by '\t'


sqoop export \
--connect "jdbc:mysql://192.168.11.81:3306/querydb?useUnicode=true&characterEncoding=utf-8" \
--username root \
--password 123456 \
--table query1 \
--export-dir /user/hive/warehouse/db_job.db/query1 \
--input-fields-terminated-by '\001'


$.ajax({
  type:'get',
  url:'/company/a',
  data:{key_0:key_0},
})