# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-29 14:15:39
# @Last Modified time: 2019-04-29 14:15:39
from Api_Manager import db
from Api_Manager.model.user_model import User,Role
# ro1=Role(name='admin')
# db.session.add(ro1)
# db.session.commit()
user1=User(username='dangkai',email='1370465454@qq.com',password='123456',role_id=None)
db.session.add(user1)
db.session.commit()
# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config['DATABASE'],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row
#
#     return g.db
#
# def close_db(e=None):
#     db = g.pop('db', None)
#
#     if db is not None:
#         db.close()