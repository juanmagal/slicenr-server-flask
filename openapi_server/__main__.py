#!/usr/bin/env python3

import connexion

import os

import logging

from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from jsonschema import ValidationError

from .helpers.resourceDb import ResourceDb
from .helpers.serviceProfileDb import ServiceProfileDb

from . import db

def main():

    __tablename__ = 'resource_db'
    __tablename__ = 'service_profile_db'
    __tablename__ = 'slice_profile_db'

    basedir = os.path.abspath(os.path.dirname(__file__))

    app = connexion.App(__name__, specification_dir='./openapi/')
    flaskapp = app.app # Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Provisioning MnS'},
                pythonic_params=True,strict_validation=True,validate_responses=True)
    app.add_api('openapi1.yaml',
                arguments={'title': 'NS Provisioning MnS'},
                pythonic_params=True)
    app.add_api('openapi2.yaml',
                arguments={'title': 'NSS Provisioning MnS'},
                pythonic_params=True)
    flaskapp.config.from_mapping(
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    )

    app.add_error_handler(ValidationError,bad_request_error_handler)

    db.init_app(flaskapp)

    with flaskapp.app_context():
       db.create_all()

    # print(db.get_tables_for_bind())

    app.run(port=8080, debug=True)


def bad_request_error_handler(error):
    v = 1

if __name__ == '__main__':
    main()
