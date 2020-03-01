from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
import time

# socket = TSocket.TSocket('zhuboo.cn', 14121)
socket = TSocket.TSocket('192.168.2.121', 9090)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
socket.open()

print(client.getTableNames())
table_name = "job_db.job_h"
print(client.getColumnDescriptors(table_name))
# client.disableTable(table_name)
# client.deleteTable(table_name)
# print(client.getTableNames())

# scannerId = client.scannerOpen('test','row1',["cf1:b","cf2:a"])   # 在指定表中，从指定行开始扫描，到表中最后一行结束，扫描指定列的数据。
# scannerId = client.scannerOpenTs('test','row1',["cf1:b","cf2:a"],timestamp=1513579065365)  # 在指定表中，从指定行开始扫描，获取所有小于指定时间戳的所有数据，扫描指定列的数据
# scannerId = client.scannerOpen(table_name, '0980001', ["info:j_name", "info:salary_range", 'info:j_t', 'info:j_e', 'info:c_size'])   # 在指定表中，从指定行开始扫描，扫描到结束行结束(并不获取指定行的数据)，扫描指定列的数据
# scannerId = client.scannerOpenWithStopTs('test','row1','row2',["cf1:b","cf2:a"],timestamp=1513579065365)  # 获取所有小于指定时间戳的所有数据
# scannerId = client.scannerOpenWithPrefix('test','row',["cf1:b","cf2:a"])   #在指定表中，扫描具有指定前缀的行，扫描指定列的数据
#
# a = time.time()
# count = 0
# while True:
#     result = client.scannerGet(scannerId)   # 根据ScannerID来获取结果
#     if not result:
#         break
#     count += 1
# b = time.time() - a
# print(count, b)


# result = client.scannerGetList(scannerId, 100)   # 根据ScannerID来获取指定数量的结果
# for i in result:
#     print(i)
# print(result)

# client.scannerClose(scannerId)  # 关闭扫描器

socket.close()  # 关闭连接

