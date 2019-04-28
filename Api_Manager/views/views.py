# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 17:19:27
# @Last Modified time: 2019-04-28 17:19:27
from Api_Manager import server

@server.route('/')
@server.route("/index")
def index():
    user = {'username':'Andy'}
    return '''<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['username'] + '''</h1>
  </body>
</html>'''
