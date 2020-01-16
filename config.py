import os,mysql.connector

class Config():
    SECRET_KEY = 'Wen hai yan and Unice' or os.environ.get('SECRET_KEY') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UNICE_ADMIN = os.environ.get('UNICE_ADMIN') or '15078843336@163.com'


    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    DEBUG = True  # 启动Flask的Debug模式
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:HUANGzeng123@localhost/unice-dev'   #数据库连接

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:HUANGzeng123@localhost/unice-test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:HUANGzeng123@localhost/unice'

config = {
    'development':Development,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':Development
}