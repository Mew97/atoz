import os
from flask import Flask
from atoz.blueprints.index import index_bp
from atoz.blueprints.faqs import faqs_bp
from atoz.blueprints.area import area_bp
from atoz.blueprints.company import company_bp
from atoz.blueprints.contact import contact_bp

from atoz.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('atoz')

    app.config.from_object(config[config_name])

    # register_extensions(app)
    register_blueprints(app)
    # register_commands(app)

    return app


def register_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(faqs_bp, url_prefix='/faqs')
    app.register_blueprint(area_bp, url_prefix='/area')
    app.register_blueprint(company_bp, url_prefix='/company')
    app.register_blueprint(contact_bp, url_prefix='/contact')






