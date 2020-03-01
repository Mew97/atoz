# from atoz.utils import impala_s, result_l, result_3d
import json
import pypinyin

# sql = "select j_t, j_e from job_t group by area;"
# sql1 = "select j_t, j_e, count(*) from job_t group by j_t, j_e;"
# x, y = impala_s(sql1)
# print(x, y)
# print(result_3d(x, x1, y1))

# 外网穿透
#
# host/ip: zhuboo.cn
# port: 5位数字，前2位数字表示服务（11代表ssh，12代表impala， 13代表mysql），后3位数字表示哪个cdh（121～125）
#
# 例如：
# ssh连接chd1 ip地址为：zhuboo.cn  端口为：11121
# ssh连接chd3 ip地址为：zhuboo.cn  端口为：11123
# 连接cdh1的mysql host为：zhuboo.cn 端口为：13121
# 连接cdh3的impala host为：zhuboo.cn 端口为：12123

# print(b'\xE5\xB9\xB4'.decode('utf-8'))

a = {'a':1, 'b':2}
if a == {'b':2, 'a':1}:
    print('a')
print(''.join(pypinyin.lazy_pinyin('湖北省')))

assert