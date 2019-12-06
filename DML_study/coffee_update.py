from DML_study.connection_pool import Connection_Pool
from mysql.connector import Error


def update_product(sql,code,name):
    args=(code,name)
    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()