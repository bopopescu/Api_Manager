# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 18:12:53
# @Last Modified time: 2019-04-28 18:12:53
from flask import render_template,flash,redirect,url_for,request
from Api_Manager import server,db
from Api_Manager.controller.login_form import LoginForm,Register
from Api_Manager.model.user_model import User,Role

@server.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    return render_template('/main/login.html',title="登录",form=form)

@server.route('/register',methods=['GET','POST'])
def register():
    form=User()
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        sex=request.form['sex']
        age=request.form['age']
        email = request.form['email']
        error = None
        if not user:
            error = 'Username is required.'
        elif not pwd:
            error = 'Password is required.'

        if error is None:
            new_user=User(username=user,password=pwd,sex=sex,age=age,email=email)
            db.session.add(new_user)
            db.session.commit()
            #保存数据到数据库中
            return redirect(url_for('login'))

        flash(error)

    return render_template('/main/register.html',form=form)