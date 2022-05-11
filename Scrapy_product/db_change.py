#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@File        : 
@Project     : aiostarlord
@Time        : 2021/8/13 11:02
@Author      : RuanJieHui
@Software    : PyCharm
@issue       : 
@change      : 
@reason      : 
"""

import logging
import traceback
import aiomysql
import pymysql.err

logging.basicConfig(level=logging.DEBUG,  # 设置日志显示级别
                    filename="test1.log",
                    format='%(asctime)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%A, %d %B %Y %H:%M:%S',  # 指定日期时间格式
                    )  # 指定handler使用的日志显示格式


class Aiomysql_DbHelper(object):

    def __init__(self, host, user, pwd, db):
        # self._conn = None
        # self._cursor = None
        self._pool = None
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __new__(cls, *args, **kwargs):
        if not hasattr(Aiomysql_DbHelper, '_instance'):
            Aiomysql_DbHelper._instance = object.__new__(cls)
        return Aiomysql_DbHelper._instance

    async def get_pool(self):
        if not self._pool:
            self._pool = await aiomysql.create_pool(host=self.host, port=3306,
                                                    user=self.user, password=self.pwd,
                                                    db=self.db)
        return self._pool

    async def fetch(self, sql, data=None, excutemany=0):
        try:
            pool = await self.get_pool()
            async with pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cursor:
                    try:
                        if not excutemany:
                            res = await cursor.execute(sql, data)
                        else:
                            res = await cursor.executemany(sql, data)
                        await conn.commit()
                        if 'select' in sql:
                            return await cursor.fetchall()
                        return res
                    except pymysql.err.IntegrityError as e:
                        await conn.rollback()
                        logging.info(f"mysql insert 异常：{traceback.format_exc()}")
                    except:
                        await conn.rollback()
                        logging.info(f"mysql {sql.split(' ')[0]} 异常：{traceback.format_exc()}")
        except ConnectionError and pymysql.err.OperationalError as ce:
            logging.info(f"mysql 链接 异常：{traceback.format_exc()}")
        except:
            logging.info(f"mysql {sql.split(' ')[0]} 异常：{traceback.format_exc()}")

    def __repr__(self):
        return f'Aiomysql_DbHelper(主机:{self.host}, 用户名:{self.user}, 数据库:{self.db})'

    __str__ = __repr__
if __name__ == '__main__':
    db = Aiomysql_DbHelper(host='localhost', user='root', pwd='123456789', db='qiushi')
    db2 = Aiomysql_DbHelper(host='localhost', user='root', pwd='123456789', db='qiushi')
    print(id(db),id(db2))
    print(type(db))