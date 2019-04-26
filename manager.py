# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-26 16:25:11
# @Last Modified time: 2019-04-26 16:25:11
# 可以通过修改route()修饰器实现不同的url解析，比如，我们改成如下的样子
from Api_Manager import app
from flask import render_template
# @app.route('/')
# @app.route('/index')
# def login():
#     return render_template('Api_Manager/templates/login.html', title="主页")
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)