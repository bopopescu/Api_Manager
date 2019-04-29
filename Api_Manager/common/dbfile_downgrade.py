# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-29 09:28:15
# @Last Modified time: 2019-04-29 09:28:15
#回滚数据库
from migrate.versioning import api
from Api_Manager.config.setting import Config,TestingConfig
v = api.db_version(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
api.downgrade(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO, v - 1)
print('Current database version: ' + str(api.db_version(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)))