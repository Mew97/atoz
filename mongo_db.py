import pymongo, time
import sys
# import scrapyd_api
# from scrapyd_api import ScrapydAPI
# import scrapyd_api

# start = time.time()
# client = pymongo.MongoClient("mongodb://zhubo:zb52971552@101.132.117.61:27017/admin")  # Alice
# client = pymongo.MongoClient("mongodb://zhubo:zb52971552@203.195.224.50:27017/admin")  # Arthur
client = pymongo.MongoClient("mongodb://hadoop:hadoop@192.168.11.33:27017/admin")  # hadoop3
# client = pymongo.MongoClient(host='129.28.67.74', port=27017)
# client = pymongo.MongoClient(host='198.181.32.215', port=27017)
# client = pymongo.MongoClient(host='101.132.117.61', port=27017)
# client.admin.authenticate('zhubo', '529715')  # 这一步是用户认证，用户跟着数据库走，所以必须在对应的数据库下认证
# a = client.list_database_names()  # 列举所有的数据库出来
# db = client['tutorial']  # 选择一个数据库
db = client['hive1']  # 选择一个数据库
# db.create_collection('students')  # 创建一个集合
# b = db.list_collection_names()  # 列举改数据库所有的集合
# account = db.get_collection(db.list_collection_names()[0])  # 选择一个集合
# account = db['51job1']  # 选择一个集合
collection = db['big_t']

# i1 = account.find_one() # 找出集合中的某一项
# i = account.find(projection={'_id': False}).limit(10)
# end = time.time()
# print(a)
# print(account)
# print(i.next())
# for j in i:
#     print(j)
#

# filename = sys.argv[1]
#
# with open(filename, 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         info_d = {}
#         info_d.setdefault('info', line.strip())
#
#         collection.insert(info_d)
#     f.close()


# search = {'$or': [
#     {'j_cate_s': {'$in': ['python', 'java']}},
#     {'j_responsibilities': {'$regex': '.*职责.*'}}
# ]}

search = {
    'info': {'$regex': '^(?=.*大数据)(?=.*美女)(?=.*python).*'},

}

res = collection.find(search)

count = 0
sum = 0
for i in res:
    print(i)
    count += 1
    if count > 100:
        break

# for i in res:
#     count += 1
#     sum += float(i['salary_range'])
#
#
# print(sum/count)

# sum = 0
# f = open('amazon.txt', 'w', encoding='UTF-8')
# for item in db['project'].find(projection={'_id': False}):
#     sum += 1
#     for key in item:
#         if item[key]:
#             f.write(item[key].strip() + '\t')
#         else:
#             f.write('数据缺失' + '\t')
#     f.write('\n')
# f.close()
# print(sum)

# print(end - start)
# db.drop_collection('QuoteItem')
client.close()
# db.drop_collection('students')  # 删除一个集合
# client = pymongo.MongoClient(host='127.0.0.1', port=27017)


