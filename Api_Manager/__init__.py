# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-26 16:32:38
# @Last Modified time: 2019-04-26 16:32:38
#导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask
#导入自定义配置
from Api_Manager.config.setting import config
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_login import LoginManager
#做登录校验
# login_manager=LoginManager()
# #login_manager.login_view = "main.login" 指定了未登录时跳转的页面，即被拦截后统一跳到user/login这个路由下
# login_manager.login_view="user.login"
server=Flask(__name__)
# server=login_manager.init_app(app)
server.config.from_object(config['default'])
db = SQLAlchemy(server)
# manager=Manager(server)
# migrate=Migrate(server,db)
# manager.add_command('db',MigrateCommand)
from Api_Manager.views import views,login_view,register_view
from Api_Manager.model import user_model