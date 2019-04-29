# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-04-28 11:42:12
# @Last Modified time: 2019-04-28 11:42:12
#迁移数据
import importlib,imp
from migrate.versioning import api
from Api_Manager import db
from Api_Manager.config.setting import Config,TestingConfig
migration = Config.SQLALCHEMY_MIGRATE_REPO + '\\versions\\%03d_migration.py' % (api.db_version(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO) + 1)
print(api.db_version(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
exec(old_model,tmp_module.__dict__)
script = api.make_update_script_for_model(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
# a = api.upgrade(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as ' + migration)
print('Current database version: ' + str(api.db_version(TestingConfig.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)))