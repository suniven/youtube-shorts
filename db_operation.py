import pymysql

# 创建db连接
conn = pymysql.connect(host='localhost', user='root', password='1101syw', database='youtube_shorts')
cursor = conn.cursor()
# 定义sql语句
sql = """

"""

# 执行sql
cursor.execute(sql)

# 关闭cursor
cursor.close()

# 关闭db连接
conn.close()
