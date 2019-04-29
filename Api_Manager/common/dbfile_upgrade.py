# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-29 09:26:16
# @Last Modified time: 2019-04-29 09:26:16
#升级数据库版本
from migrate.versioning import api
from Api_Manager.config.setting import Config,TestingConfig
api.upgrade(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(api.db_version(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)))