from mysql.connector import Error
from DML_study.connection_pool import Connection_Pool


def transaction_fail1():

    try:
        print('Connectin to MySQL database.......')
        conn = Connection_Pool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit =False
        cursor = conn.cursor()
        insert_sql = "insert into product values (%s,%s)"
        cursor.execute(insert_sql,('A001','아메리카노'))
        cursor.execute(insert_sql,('C004','라떼4'))
        print("Record 2 product successfully")
        conn.commit()
    except Error as error:
        print ("Failed to update record to database rollback: {}".format(error))
        conn.rollback()

    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")




def transaction_fail2():

    try:
        print('Connectin to MySQL database.......')
        conn = Connection_Pool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit =False
        cursor = conn.cursor()
        insert_sql = "insert into product values (%s,%s)"
        cursor.execute(insert_sql,('D001','아메리카노 Set'))
        cursor.execute(insert_sql,('C001','라떼1'))
        print("Record 2 product successfully")
        conn.commit()
    except Error as error:
        print ("Failed to update record to database rollback: {}".format(error))
        conn.rollback()

    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")



def transaction_success():

    try:
        print('Connectin to MySQL database.......')
        conn = Connection_Pool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit =False
        cursor = conn.cursor()
        insert_sql = "insert into product values (%s,%s)"
        cursor.execute(insert_sql,('D001','아메리카노 Set'))
        cursor.execute(insert_sql,('C005','라떼5'))
        print("Record 2 product successfully")
        conn.commit()
    except Error as error:
        print ("Failed to update record to database rollback: {}".format(error))
        conn.rollback()

    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")