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

server=Flask(__name__)
server.config.from_object(config['default'])
db = SQLAlchemy(server)
from Api_Manager.views import views,login_view
from Api_Manager.model import user_model