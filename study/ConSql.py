import pymssql
import pymysql
import xlwt
conn = pymssql.connect('localhost', 'sa', 'sasa', 'RAPIDPATH')  # 连接sql server数据库
conn1 = pymysql.connect('192.168.88.129', 'root', 'sasa', 'MES')  # 连接mysql数据库
if conn:
    print("数据库连接成功！")
if conn1:
    print("数据库1连接成功！")
cursor = conn.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
sql = "select top 10 * from [dbo].[PATH_Equipment]"
cursor.execute(sql)  # 执行sql语句

# row = cursor.fetchone()  # 读取一行查询结果
row = cursor.fetchall()  # 读取一行查询结果

def1 = cursor.description

wk = xlwt.Workbook()
sheet = wk.add_sheet("测试")
# print(row)
for j in range(0, len(def1)):
    sheet.write(0, j, def1[j][0])
i = 0
while i < len(row):
    #   print(row[1][0])
    for j in range(0, len(row[0])):
        sheet.write(i+1, j, row[i][j])
        # print(row[i][j])
    i += 1
#    row = cursor.fetchone()

wk.save("d://su1shi2.xls")

cursor.close()  # 关闭游标
conn.close()  # 关闭连接

