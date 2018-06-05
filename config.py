import os

class Config(object):
    # WTF_CSRF_ENABLED = True
    SECRETE_KEY = 'my_secret_key'
    # -- CONFIG EMAIL PARAMS (enviador de correos)
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_SSL = False
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'micorreo@gmail.com'
    # MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')

class DevelopmentConfig(Config):
    DEBUG = True
    # WTF_CSRF_ENABLED = True
    SECRET_KEY = 'my_secret_key'
    # UPLOAD_FOLDER = '/Uploads'
    # SQLALCHEMY_DATABASE_URI = 'motorDB://root:password@localhost/db' # -- sin password
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///applicants.sqlite3'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flask' # -- con password
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_tutorial' # -- sin password
    SQLALCHEMY_TRACK_MODIFICATIONS = False # -- notificaciones warning
    # FILE_TYPES = ['txt', 'doc', 'docx', 'odt', 'pdf', 'rtf', 'text', 'wks', 'wps', 'wpd']
