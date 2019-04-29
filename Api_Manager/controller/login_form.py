# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 11:42:12
# @Last Modified time: 2019-04-28 11:42:12
from flask_wtf import FlaskForm as Form
from wtforms import StringField,PasswordField,SubmitField,ValidationError,RadioField,BooleanField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from Api_Manager.model import user_model

class LoginForm(Form):
    """登录表单"""
    username=StringField(label='用户名',validators=[DataRequired('username is null'),Length(min=6, max=12, message='长度为6-12位')],render_kw={'placeholder': '请输入用户名...', 'maxlength': 12})
    password=PasswordField(label='密码',validators=[DataRequired('password is null'),Length(min=6, max=12, message='长度为6-12位')],render_kw={'placeholder': '请输入用户名...', 'maxlength': 12})
    submit = SubmitField('登录')



class Register(Form):
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空...'),Length(min=6,max=12,message='长度为6-12位')],render_kw={'placeholder':'请输入用户名...','maxlength':12})
    password = PasswordField('密码',validators=[DataRequired(message='密码不能为空'),Length(min=6,max=12,message='长度为6-12位'),EqualTo('confirm',message='俩次密码不一致')],render_kw={'placeholder':'请输入密码...','maxlength':12})
    sex=RadioField('性别',choices=((0,'男'),(1,'女')))
    age=StringField('用户名',validators=[Length(min=6,max=12,message='长度为6-12位')],render_kw={'placeholder':'请输入年龄','maxlength':5})
    nickname=StringField('姓名',validators=[DataRequired(message='姓名不能为空...'),Length(min=4,max=8,message='长度为4-8位')],render_kw={'placeholder':'请输入姓名...','maxlength':8})
    confirm = PasswordField('确认密码',validators=[DataRequired(message='确认密码不能为空'),Length(min=6,max=12,message='长度为6-12位'),EqualTo('password',message='两次密码不一致')],render_kw={'placeholder':'请输入确认密码...','maxlength':12})

    email = StringField('邮箱',validators=[Email(message='请输入正确的邮箱')],render_kw={'placeholder':'请输入邮箱...','maxlength':30})
    submit = SubmitField('注册')

    # 自定义验证器 用户名是否存在
    def validate_username(self, field):
        if user_model.query.filter(user_model.username == field.data).first():
            raise ValidationError('该用户已注册!!!')

    # 自定义验证器 邮箱是否存在
    def validate_email(self, field):
        if user_model.query.filter(user_model.email == field.data).first():
            raise ValidationError('该邮箱已注册!!!')
