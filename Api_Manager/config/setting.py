# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 16:24:57
# @Last Modified time: 2019-04-28 16:24:57
import os
# 所有环境配置的基类
class Config:
    # Flask - WTF需要用到的2个配置项。CSRF_ENABLED配置启用了跨站请求攻击保护，大部分情况下你都需要开启此功能，这能使你的应用更安全
    CSRF_ENABLED=True
    # SECRET_KEY设置当CSRF启用时有效，这将生成一个加密的token供表单验证使用，你要确保这个KEY足够复杂
    SECRET_KEY = 'secret_key'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 为迁移数据库创建目录db_repository
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    #邮箱发送配置
    MAIL_SERVER =  os.environ.get('MAIL_SERVER','smtp.163.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','13545273328@163.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','dk137046')
    #数据库信息
    HOSTNAME = "127.0.0.1"
    PORT = "3306"
    DATABASE = "apimanager"
    USERNAME = "root"
    PASSWORD = "137046"
#测试配置这里数据库原本是utf8改为gbk
class TestingConfig(Config):
    """配置参数 SQLALCHEMY_DATABASE_URI用于连接数据库，SQLALCHEMY_ECHO如果设置成 True，SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助"""
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=gbk".format(Config.USERNAME, Config.PASSWORD, Config.HOSTNAME, Config.PORT, Config.DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

#开发配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=gbk" .format(Config.USERNAME, Config.PASSWORD, Config.HOSTNAME, Config.PORT, Config.DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

#生产配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=gbk" .format(Config.USERNAME, Config.PASSWORD, Config.HOSTNAME, Config.PORT, Config.DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
#一个配置的字典
config = {
    #开发环境
    'development':DevelopmentConfig,
    #生产环境
    'production':ProductionConfig,
    #测试环境
    'test':TestingConfig,
    'default':TestingConfig
}
