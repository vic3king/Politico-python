import os
import sys
import json
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
from api.party.models import Party
from api.office.models import Office


# Fixtures
from fixtures.token.token_fixture import CITIZEN_TOKEN, ADMIN_TOKEN
sys.path.append(os.getcwd())


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/graphql'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            admin_user = User(first_name="doe",
                              last_name="jon",
                              other_names="smith",
                              email="admin@yahoo.com",
                              password="12345678",
                              picture="https://picsum.photos/200",
                              user_type="admin")

            admin_user.save()
            citizen_user = User(first_name="doe",
                                last_name="jon",
                                other_names="smith",
                                email="citizen@yahoo.com",
                                password="12345678",
                                picture="https://picsum.photos/200",
                                user_type="citizen")

            citizen_user.save()
            politician_user = User(first_name="doe",
                                   last_name="jon",
                                   other_names="smith",
                                   email="politician@yahoo.com",
                                   password="12345678",
                                   picture="https://picsum.photos/200",
                                   user_type="politician")

            politician_user.save()
            party = Party(party_name="party",
                          hq_address="5 City Of Power Avenue, Somolu, Lagos, Nigeria",  # noqa
                          logo_url="www.ipsum/pic")
            party.save()
            office = Office(office_name="office",
                            office_type="state",
                            age_limit=50,
                            description="my testing office")
            office.save()
            db_session.commit()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)


class CommonTestCases(BaseTestCase):
    """Common test cases throught the code.
    This code is used to reduce duplication
    :params
        - loggedin_CITIZEN_TOKEN_assert_equal
    """

    def citizen_token_assert_equal(self, query, expected_response):
        """
        Make a request with verified citizen token and use assertEquals
        to compare the values
        :params
            - query, expected_response
        """

        headers = {"Authorization": "Bearer" + " " + CITIZEN_TOKEN}
        response = self.app_test.post(
            '/graphql?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def admin_token_assert_equal(self, query, expected_response):
        """
        Make a request with verified admin token and use assertEquals
        to compare the values
        :params
            - query, expected_response
        """

        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/graphql?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)
