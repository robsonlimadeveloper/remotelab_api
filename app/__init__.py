import os
from typing import List, Dict
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow
from flask_injector import FlaskInjector
from flask_swagger_ui import get_swaggerui_blueprint

from .middleware.middleware import Middleware
from .seeds.seeder import Seeds
from app import modules

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

ma = Marshmallow(app)
app.wsgi_app = Middleware(app.wsgi_app)

seeder = Seeds(db, modules)

@app.cli.command()
def seed():
    """Seed datas from here"""
    seeder.run()

from app.core import routes, handler_error

FlaskInjector(app)

API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    os.environ["SWAGGER_URL"],
    os.environ["API_URL"],
    config={
        'app_name': 'Remotelab'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=os.environ["SWAGGER_URL"])

if __name__ == '__main__':
    manager.run(host='0.0.0.0', port=4010)
