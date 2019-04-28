# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 19:11:57
# @Last Modified time: 2019-04-28 19:11:57
from Api_Manager import db
#这个是必须要的
from Api_Manager.model import user_model


if __name__ == '__main__':
    '''清除数据库中的所有数据'''
    db.drop_all()
    '''创建所有表'''
    db.create_all()