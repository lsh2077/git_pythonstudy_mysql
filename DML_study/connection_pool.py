import mysql
from mysql.connector.pooling import MySQLConnectionPool


class Connection_Pool(object):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            self.__cnxPool = MySQLConnectionPool(pool_name="myPool", pool_size=5, option_files='db_Config.conf')

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = Connection_Pool()
        return cls.INSTANCE;

    def get_connection(self):
        return self.__cnxPool.get_connection()

    @classmethod
    def pool_close(cls):
        cls.INSTANCE = None