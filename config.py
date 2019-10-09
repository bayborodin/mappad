import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://mappad:mappad@localhost/mappad'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN_NAME = os.environ.get('DOMAIN_NAME')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLC') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    REPORT_EMAIL = os.environ.get('REPORT_EMAIL')
