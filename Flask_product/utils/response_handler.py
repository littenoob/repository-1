# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/8 17:35
@Author ： jiafei
@email ： 1723957366@qq.com
@File ：response_handler.py
@feature：xxx
"""
from flask import make_response
import json
def sqlResult2json(sqlResult):
    return json.dumps([{'brand': item.brand, 'type': item.type} for item in sqlResult])

def err_response(information):
    return make_response(json.dumps({'err':information}))