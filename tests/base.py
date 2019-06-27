import os
import sys

# Packages
from flask_testing import TestCase
from graphene.test import Client
from alembic import command, config

# Setup
from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base

# Models
from api.user.models import User

sys.path.append(os.getcwd())


class BaseTestCase(TestCase):
    alembic_configuration = config.Config("./alembic.ini")

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/politico'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            command.stamp(self.alembic_configuration, 'head')
            command.downgrade(self.alembic_configuration, '-1')
            command.upgrade(self.alembic_configuration, 'head')
            admin_user = User(first_name="doe",
                              last_name="jon",
                              other_names="smith",
                              email="admin@yahoo.com",
                              password="12345678",
                              picture="https://picsum.photos/200",
                              user_type="admin")

            admin_user.save()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
            db_session.remove()
            # Base.metadata.drop_all(bind=engine)
