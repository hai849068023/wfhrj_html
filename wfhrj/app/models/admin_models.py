# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/9/25 13:26'
# 导入模块
from app import db


class Farmers(db.Model):
    __tablename__ = 'farmers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(4), nullable=False, index=True, comment='农家主名字')
    tel = db.Column(db.String(11), nullable=False, comment='电话')
    address = db.Column(db.String(50), nullable=False, index=True, comment='农家地址')
    portrait = db.Column(db.String(200), comment='头像')
    qualification = db.Column(db.String(20), comment='农主资质个人或者商户')
    goods = db.relationship('Goods', backref='farmers')


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(4), nullable=False, index=True, comment='商品名称')
    image = db.Column(db.String(200), nullable=False, comment='商品图片')
    price = db.Column(db.String(10), nullable=False, comment='商品价格')
    line_price = db.Column(db.String(10), nullable=False, comment='划线价格')
    is_shelves = db.Column(db.Boolean, comment='是否上架')
    farmers_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), comment='农户外键字段')
