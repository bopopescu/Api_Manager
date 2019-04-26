# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-26 17:39:04
# @Last Modified time: 2019-04-26 17:39:04
from Api_Manager import db
from Api_Manager.model.User import User,Role


if __name__ == '__main__':
    '''清除数据库中的所有数据'''
    db.drop_all()
    '''创建所有表'''
    db.create_all()
    # # 给用户身份表中添加两个数据
    # '''创建一个对象'''
    # role1 = Role(name="admin")
    # '''在Flask-SQLAlchemy中，插入、修改、删除操作，均由数据库会话管理。会话用db.session表示'''
    # '''session 记录对象任务 '''
    # db.session.add(role1)
    # '''提交任务到数据库中'''
    # db.session.commit()
    #
    # role2 = Role(name="stuff")
    # db.session.add(role2)
    # db.session.commit()
    #
    # # 给用户表中添加数据
    # us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    # us2 = User(name='zhang', email='zhang@189.com', password='452342', role_id=role2.id)
    # us3 = User(name='chen', email='chen@126.com', password='782677', role_id=role2.id)
    # us4 = User(name='zhou', email='zhou@163.com', password='858585', role_id=role1.id)
    # '''一次性添加多条数据'''
    # db.session.add_all([us1, us2, us3, us4])
    # db.session.commit()