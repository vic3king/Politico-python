from tests.base import BaseTestCase
from fixtures.user.login_user_fixture import (
    login_user_query,
    login_user_response,
    login_user_query_incorrect_credentials,
    login_user_response_incorrect_credentials,
    login_user_query_user_not_found,
    login_user_response_user_not_found
)

from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestLoginUser(BaseTestCase):

    def test_login_user(self):
        """
        Testing for Login in a user
        """

        execute_query = self.client.execute(
            login_user_query,
            context_value={'session': db_session})

        expected_response = login_user_response
        self.assertEqual(execute_query, expected_response)

    def test_login_user_with_incorrect_credentials(self):
        """
        Test for Loggin in a user with incorrect details
        """

        execute_query = self.client.execute(
            login_user_query_incorrect_credentials,
            context_value={'session': db_session})

        expected_response = login_user_response_incorrect_credentials
        self.assertEqual(execute_query, expected_response)

    def test_login_user_not_founf(self):
        """
        Test for Loggin in a user that doesnt exist
        """

        execute_query = self.client.execute(
            login_user_query_user_not_found,
            context_value={'session': db_session})

        expected_response = login_user_response_user_not_found
        self.assertEqual(execute_query, expected_response)
