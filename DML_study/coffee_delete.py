from DML_study.connection_pool import Connection_Pool
from mysql.connector import Error


def delete_product(sql,code):

    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql,(code,))
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()