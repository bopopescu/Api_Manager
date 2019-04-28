# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 16:24:57
# @Last Modified time: 2019-04-28 16:24:57
import os
#所有环境配置的基类
class Config:
    SECRET_KEY = 'dk137046'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER =  os.environ.get('MAIL_SERVER','smtp.163.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','13545273328@163.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','dk137046')
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "apimanager"
USERNAME = "root"
PASSWORD = "137046"
#测试配置这里数据库原本是utf8改为gbk
class TestingConfig(Config):
    """配置参数 SQLALCHEMY_DATABASE_URI用于连接数据库，SQLALCHEMY_ECHO如果设置成 True，SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助"""
    SQLALCHEMY_DATABASE_URI = '"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db}?charset=gbk". \
        format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

#开发配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:20111673@127.0.0.1:3306/blogModel'

#生产配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:2011673@127.0.0.1:3306/development'
#一个配置的字典
config = {
    #开发环境
    'development':DevelopmentConfig,
    #生产环境
    'production':ProductionConfig,
    #测试环境
    'test':TestingConfig,
    'default':DevelopmentConfig
}
