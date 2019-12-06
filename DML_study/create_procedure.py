from mysql.connector import Error,errorcode
from DML_study.connection_pool import Connection_Pool



PROCEDURE_NAME = 'proc_sale_stat'
PROCEDURE_SQL = """
                CREATE PROCEDURE proc_sale_stat()
                BEGIN
                    select  sum(@saleprice := price*salecnt) sale_price,
                            sum(@addtax := ceil(@saleprice/11)) addtax_price,
                            sum(@supprice := @saleprice - @addtax) supply_price,
                            sum(@marprice := round(@supprice * (marginrate/100))) margin_price
                        from sale s join product p on s.code = p.code;
                END
                """

def create_procedure():
    try:
        conn = Connection_Pool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(PROCEDURE_SQL)
        print("CREATE PROCEDURE {}".format(PROCEDURE_NAME))
    except Error as err:
        if err.errno == errorcode.ER_SP_ALREADY_EXISTS:
            cursor.execute("DROP PROCEDURE {}".format(PROCEDURE_NAME))
            print("DROP PROCEDURE {}".format(PROCEDURE_NAME))
            cursor.execute(PROCEDURE_SQL)
            print("CREATE PROCEDURE {}".format(PROCEDURE_NAME))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()