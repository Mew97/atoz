# -*-coding:utf-8-*-
import os
import sys


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    SQL_DB = ['192.168.2.121', 'root', '123456']
    IMPALA = ['192.168.2.123', 21050]


class DevelopmentConfig(BaseConfig):
    pass
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:zb52971552@47.101.214.54/merapy_db?charset=utf8"


class ProductionConfig(BaseConfig):
    pass
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://localhost/merapy_db?charset=utf8"


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
