# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/9/20 15:24'
# 导入模块

from flask import Flask
from app.admin.admin_home import admin
from app.admin.admin_farmers import farmers
from flask_sqlalchemy import SQLAlchemy

# 蓝图注册
app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(farmers, url_prefix='/farmers')


# 配置flask配置对象中键：SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1/wfhrj"

# 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)

