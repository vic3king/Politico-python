from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.party.party_fixture import (
    allParties_query,
    allParties_query_response,
    single_party_query,
    single_party_query_not_found,
    single_party_query_not_found_response,
    single_party_query_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryParty(BaseTestCase):

    def test_get_all_parties(self):
        """
        Testing query to return all parties
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            allParties_query,
            allParties_query_response
        )

    def test_get_party(self):
        """
        Testing query to return a party
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            single_party_query,
            single_party_query_response
        )

    def test_get_party_not_found(self):
        """
        Testing query to return a party when not found
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            single_party_query_not_found,
            single_party_query_not_found_response
        )
