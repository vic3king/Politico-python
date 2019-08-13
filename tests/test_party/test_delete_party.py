from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.party.party_fixture import (
    delete_party_mutation,
    delete_party_mutation_response,
    delete_party_does_not_exist_mutation,
    delete_party_does_not_exist_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateParty(BaseTestCase):

    def test_delete_party_mutation(self):
        """
        Testing mutation to delete a party
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            delete_party_mutation,
            delete_party_mutation_response
        )

    def test_delete_party_does_not_exist_mutation(self):
        """
        Testing mutation to delete a party that does not exist
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            delete_party_does_not_exist_mutation,
            delete_party_does_not_exist_response
        )
