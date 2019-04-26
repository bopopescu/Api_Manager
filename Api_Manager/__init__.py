# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-26 16:32:38
# @Last Modified time: 2019-04-26 16:32:38
#导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from Api_Manager.model import User
#导入数据库模块
# import pymysql
#默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块

#创建了flask实例
app = Flask(__name__)
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "apimanager"
USERNAME = "root"
PASSWORD = "137046"
class Config(object):
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db}?charset=gbk". \
        format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config.from_object(Config)
db=SQLAlchemy(app)
