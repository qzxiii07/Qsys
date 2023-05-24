# config.py
# 环境配置
ENV = 'prod'
# 数据库配置
# app/models/__init__.py
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'mydatabase'
MYSQL_USER = 'root' 
MYSQL_PASSWORD = 'admin123'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(object):
    DEBUG = True

class ProductionConfig(object):
    DEBUG = False

class TestingConfig(object):
    DEBUG = True
    TESTING = True