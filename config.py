import os

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'abcdefgh1234567890')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgres://pgqulwdclzedha:48eb104fc363ee75a99131a6b684b36758bc7fbaf87d0f8490652749b1edebd3@ec2-44-215-40-87.compute-1.amazonaws.com:5432/dc0egqt2llo2uo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'abcdefghijklmnopqrstuvwxyz1234567890')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
