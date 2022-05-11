# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/10 23:00
@Author ： jiafei
@email ： 1723957366@qq.com
@File ：api.py
@feature：xxx
"""
from flask import Flask,jsonify,make_response,request
from markupsafe import escape
from sqlalchemy import and_,or_
import json
import datetime

from models import app,phone,xiaomi
from utils.response_handler import err_response
@app.after_request
def add_allowed_orgin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'content-type: application/json; charset=utf-8'
    return response
@app.route("/brand/<name>")
def get_brand_list(name):
    if name == 'all':
        phones = phone.query.all()
    phones =  phone.query.filter_by(brand=name).all()
    return make_response(json.dumps(json.dumps([{'date':str(datetime.date.today()),'brand': item.brand,
                                                 'type': item.type,'price':'点击查看','isHot':'暂无'} for item in phones])))


@app.route("/api/v0.1/price/<tablename>")
def get_brand_price(tablename):
    if tablename.startswith('select'):
        return err_response('请停止sql注入，数据无价')
    days = request.args.get('days')
    brand = request.args.get('brand')
    if days is None or brand is None:
        return err_response('请设置dyas参数')
    now = datetime.date.today()
    res = xiaomi.query.filter(and_(xiaomi.price_date >
                              (datetime.date(now.year, now.month, now.day) - datetime.timedelta(days=int(days))),
                               xiaomi.brand == brand)).order_by(xiaomi.price_date)
    dict = {}
    data = []
    for item in res:
        if dict.get(item.price_date) is None:
            dict[item.price_date] = True
            data.append({'brand': item.brand, 'price': item.price, 'price_date': str(item.price_date),'isHot': item.isHot})
    return make_response(json.dumps(data))

@app.route("/testapi/price/xiaomi")
def get_xiaomi_price():
    xiaomis = xiaomi.query.filter(xiaomi.id == 1).first()
    return make_response(json.dumps(xiaomis.brand))
if __name__ == '__main__':
    app.run()
