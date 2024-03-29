from mysql.connector import Error
from DML_study.connection_pool import Connection_Pool

def call_sale_stat_sp(query):
    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.callproc(query)
        for result in cursor.stored_results():
            res = result.fetchone()
            print(res)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def call_order_price_by_issale(query,isSale):
    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()

        args=[isSale,]
        cursor.callproc(query,args)
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()