import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.utils import TlsSMTPHandler

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://d0595f9508754ce580ea01ca3d07000a@sentry.io/1773892",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


if not app.debug:
    logger = logging.getLogger()
    gm = TlsSMTPHandler(
        (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        'no-reply@' + app.config['DOMAIN_NAME'],
        [app.config['REPORT_EMAIL']],
        app.config['DOMAIN_NAME'] + ' - Error Report',
        (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    )
    gm.setLevel(logging.ERROR)
    logger.addHandler(gm)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/mappad.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Mappad startup')

from app import routes, models, errors
