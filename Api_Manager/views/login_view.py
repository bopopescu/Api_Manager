# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 18:12:53
# @Last Modified time: 2019-04-28 18:12:53
from flask import render_template,request,flash,session,url_for
from Api_Manager import server
from Api_Manager.controller.login_form import LoginForm
from Api_Manager.model.user_model import User
@server.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        #获取表单的用户名密码
        # username=form.username.data
        #在数据库中找
        user=User.query.filter_by(username=form.username.data).first()
        if user is not None and user.password == form.password.data:
            flash('登录成功')
            return render_template('/main/success.html',title="首页")
    return render_template('/main/login.html',title="登录",form=form)

