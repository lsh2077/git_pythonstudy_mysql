from DML_study.Fetch_Query import query_with_fetchmany
from DML_study.coffee_delete import delete_product
from DML_study.coffee_insert import insert_product, insert_products
from DML_study.coffee_procedure import call_sale_stat_sp, call_order_price_by_issale
from DML_study.coffee_select import query_with_fetchone, query_with_fetchall, query_with_fetchall2, \
    query_with_fetchall_by_code
from DML_study.coffee_update import update_product
from DML_study.connection_pool import Connection_Pool
import pandas as pd

from DML_study.create_procedure import create_procedure
from DML_study.transaction_query import transaction_fail1, transaction_fail2, transaction_success


def connection_pool_test():
    connect_pool = Connection_Pool.get_instance()
    connection = connect_pool.get_connection()
    print("connection:", connection)


def fetchone():
    sql = "select * from product"
    query_with_fetchone(sql)#한줄씩 출력


def fetchall():
    sql = "select * from product"
    query_with_fetchall(sql)#전체를 읽어와 한줄씩 출력
    res = query_with_fetchall2(sql)#천체 읽어서 res에 반환
    print(type(res), 'size=', len(res))
    for pno, pname in res:
        print(pno, pname)

def fetchall_by_code():
    product_select_where01 = "select * from product where code = %s"
    res=query_with_fetchall_by_code(product_select_where01,'A001')
    print(res)#검색 조건을 다르게 설정해서 실행

    product_select_where02="select * from product where code = '{}'".format('A001')
    query_with_fetchall((product_select_where02))
    # 검색조건을 바로 입력 실행


def fetchmany():
    sql = "select * from product"
    query_with_fetchmany(sql)#음 좋다?


def insert():
    select_sql = "select * from product"
    insert_sql = "insert into product values(%s,%s)"
    query_with_fetchall(select_sql)

    #한개 추가
    insert_product(insert_sql,'C001','라떼')
    query_with_fetchall(select_sql)
    #여러개 추가
    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]
    insert_products(insert_sql, products)
    query_with_fetchall(select_sql)


def update():
    select_sql_code = "select code,name from product where code = '{code}'".format(code='C001')
    query_with_fetchone(select_sql_code)

    update_sql = "update product set name = %s where code = %s"
    update_product(update_sql,'라떼수정','C001')

    query_with_fetchone(select_sql_code)


def delete():
    select_sql= "select code, name from product where code like 'C___'"
    res =query_with_fetchall2(select_sql)
    columns_list = ['code','name']
    df=pd.DataFrame(res,columns=columns_list)
    print(df)


    delete_sql = "delete from product where code = %s"
    delete_product(delete_sql,'C004')

    for code,name in (query_with_fetchall2(select_sql)):
        print(code,"",name)


def transaction():
    transaction_fail1()
    transaction_fail2()
    transaction_success()


def procedure():
    create_procedure()


if __name__=="__main__":
    # connection_pool_test()

#################################################
    #fetchone()
    # fetchall()
    #fetchall_by_code()
    #fetchmany()
##################################################
    #insert()
##################################################
    #update()
##################################################
    #delete()
##################################################
    #transaction()
##################################################
    # procedure()
    call_sale_stat_sp('proc_sale_stat')
    print()
    call_order_price_by_issale('proc_saledetail_orderby',False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)