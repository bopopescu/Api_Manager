# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 17:19:27
# @Last Modified time: 2019-04-28 17:19:27
from Api_Manager import server
from flask import render_template

@server.route('/')
@server.route("/index")
def index():
    user = {'username':'Andy'}
    #使用循环语句
    posts=[
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("/main/index.html",title="主页",user=user,posts=posts)
