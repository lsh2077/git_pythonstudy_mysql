from mysql.connector import MySQLConnection
try:
    con = MySQLConnection(host='localhost',database='mysql_study',user='root',password='rootroot')
    print(con)
except:
    print ()