# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 11:42:12
# @Last Modified time: 2019-04-28 11:42:12
from flask_wtf import FlaskForm as Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length


class LoginForm(Form):
    """登录表单"""
    username=StringField(label='用户名',validators=[DataRequired('username is null'),Length(min=6, max=12, message='长度为6-12位')],render_kw={'placeholder': '请输入用户名...', 'maxlength': 12})
    password=PasswordField(label='密码',validators=[DataRequired('password is null'),Length(min=6, max=12, message='长度为6-12位')],render_kw={'placeholder': '请输入用户名...', 'maxlength': 12})
    submit = SubmitField('登录')



