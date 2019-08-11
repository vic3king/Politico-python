from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.office.office_fixture import (
    allOffices_query,
    allOffices_query_response,
    single_office_query,
    single_office_query_response,
    single_office_query_not_found,
    single_office_query_not_found_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryOffice(BaseTestCase):

    def test_get_all_offices(self):
        """
        Testing query to return all offices
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            allOffices_query,
            allOffices_query_response
        )

    def test_get_office(self):
        """
        Testing query to return an office
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            single_office_query,
            single_office_query_response
        )

    def test_get_office_not_found(self):
        """
        Testing query to return an office when not found
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            single_office_query_not_found,
            single_office_query_not_found_response
        )
