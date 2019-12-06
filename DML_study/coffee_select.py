
from DML_study.connection_pool import Connection_Pool
from mysql.connector import Error


def query_with_fetchone(sql):
    try:
        conn=Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print(type(row),":",row)
            row = cursor.fetchone()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchall(sql):
    try:
        conn=Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Total Row(s):",cursor.rowcount)
        for row in rows:
            print(type(row),":",row)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchall2(sql):
    try:
        conn=Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return  cursor.fetchall()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchall_by_code(sql,code):
    args = (code,)
    try:
        conn=Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql,args)
        return  cursor.fetchall()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()