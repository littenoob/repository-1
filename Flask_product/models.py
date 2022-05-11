# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/10 23:19
@Author ： jiafei
@email ： 1723957366@qq.com
@File ：models.py
@feature：xxx
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
import datetime
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost:3306/product_information'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
class phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255),nullable=False)
    type = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class xiaomi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    price_date = db.Column(db.Date(),nullable=False)
    release_date = db.Column(db.Date())
    isHot = db.Column(db.Boolean())
    def __repr__(self):
        return '<User %r>' % self.username