#导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask
#导入数据库模块
# import pymysql
#默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import render_template
#导入前台请求的request模块
from flask import request
#创建了flask实例
app = Flask(__name__)


# 可以通过修改route()修饰器实现不同的url解析，比如，我们改成如下的样子
@app.route('/')
@app.route('/index')
def login():
    return render_template('login.html',title="主页")


# 最后调用run()方法，运行flask web应用程序
if __name__ == '__main__':
    print(__name__)
    app.run(debug=False)