from impala.dbapi import connect
import time, re
from atoz.utils import impala_s

# sql = 'select avg(salary_range) from job_t;'
# results_all = impala_s(sql)
# results, time0 = results_all[0], results_all[1]
#
# print(results, time0)

# keys = ['大数据', 'python', '美女']
# sql = 'select j_name, salary_range, city, c_name, c_welfare, j_responsibilities,j_cate_s, j_cate_l, main_business, c_size, j_t, j_e from job_t where '
# for word in keys:
#     sql += "concat(j_name, city, c_name, c_welfare, j_responsibilities, j_cate_s, j_cate_l, main_business, c_size, j_t, j_e) like '%{}%' and " .format(word)
# sql = sql[:-5] + ';'
#
# print(sql)

sql = 'select count(*) from (select id from job_t group by id) a;'
sql1 = 'select count(*) from big_t;'
sql2 = 'select count(distinct *) from big_t;'
sql3 = 'select Row_Number() over (order by id) as a, * from big_t limit 10;'
sql4 = 'select count(*) from job_t_h;'
sql5 = 'select * from job_t_h1 where area="华中" order by salary_range desc limit 1;'
res0 = impala_s(sql4)

res, time0 = res0[0], res0[1]


# infos = []
# for row in res[:100]:
#     row_l = []
#     for col in row:
#         row_l.append(col)
#     infos.append(row_l)


print(res)
print(time0)





