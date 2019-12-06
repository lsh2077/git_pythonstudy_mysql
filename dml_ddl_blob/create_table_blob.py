from mysql.connector import Error,errorcode
from DML_study.connection_pool import Connection_Pool

TABLE_NAME='images'
TABLE_SQL="""
        create table images(
            no int primary key auto_increment,
            name varchar(20) not null,
            pic longblob not null
        )
"""

def create_table():
    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(TABLE_SQL)
        print("CREATE TABLE {}".format(TABLE_NAME))
    except Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            cursor.execute("DROP TABLE {}".format(TABLE_NAME))
            print("DROP TABLE {}".format(TABLE_NAME))
            cursor.execute(TABLE_SQL)
            print("CREATE TABLE {}".format(TABLE_NAME))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()