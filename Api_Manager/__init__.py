# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-26 16:32:38
# @Last Modified time: 2019-04-26 16:32:38
#导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask

server=Flask(__name__)
from Api_Manager.views import views