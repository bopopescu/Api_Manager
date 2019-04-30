# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-29 14:09:51
# @Last Modified time: 2019-04-29 14:09:51
from Api_Manager import server,db
from Api_Manager.model.user_model import User
from flask import render_template,flash,redirect,url_for,request

@server.route('/register',methods=['GET','POST'])
def register():
    form = User()
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
            flash('注册成功，请登录')
            #保存数据到数据库中
            return redirect(url_for('login'))


        flash(error)

    return render_template('/main/register.html',form=form)