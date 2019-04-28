# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 18:12:53
# @Last Modified time: 2019-04-28 18:12:53
from flask import render_template,flash,redirect
from Api_Manager import server
from Api_Manager.controller.login_form import LoginForm

@server.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    return render_template('/main/login.html',title="登录",form=form)