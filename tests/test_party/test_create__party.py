from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.party.party_fixture import (
    party_mutation_query,
    party_mutation_response,
    party_mutation_duplication_query,
    party_mutation_duplication_response,
    party_invalid_address_mutation_query,
    party_mutation_invalid_address_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateParty(BaseTestCase):

    def test_create_party_mutation(self):
        """
        Testing mutation to create a party
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            party_mutation_query,
            party_mutation_response
        )

    def test_create_party_duplicate_name_mutation(self):
        """
        Testing mutation to create a party that already exists
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            party_mutation_duplication_query,
            party_mutation_duplication_response
        )

    def test_create_party_invalid_address_mutation(self):
        """
        Testing mutation to create a party with an invalid address
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            party_invalid_address_mutation_query,
            party_mutation_invalid_address_response
        )
