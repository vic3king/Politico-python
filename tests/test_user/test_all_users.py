from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.user.user_fixture import (
    all_users_query,
    all_users_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryAllUsers(BaseTestCase):

    def test_all_user_query(self):
        """
        Testing query to return all users
        """

        CommonTestCases.user_token_assert_equal(
            self,
            all_users_query,
            all_users_response
        )
