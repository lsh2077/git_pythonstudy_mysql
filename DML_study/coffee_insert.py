from DML_study.connection_pool import Connection_Pool
from mysql.connector import Error


def insert_product(sql,code,name):
    args=(code,name)
    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def insert_products(sql,products):

    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        for i in range(len(products)):
            cursor.execute(sql, products[i])
            conn.commit()
    except Error as e:
        print('Error:',e)

    finally:
        cursor.close()
        conn.close()
