from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.office.office_fixture import (
    office_mutation_query,
    office_mutation_response,
    office_mutation_duplication_query,
    office_mutation_duplication_query_response,
    office_mutation_query_invalid_type,
    office_mutation_query_invalid_type_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateOffice(BaseTestCase):

    def test_create_office_mutation(self):
        """
        Testing mutation to create an office
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            office_mutation_query,
            office_mutation_response
        )

    def test_create_office_duplication(self):
        """
        Testing mutation to create an office that already exists
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            office_mutation_duplication_query,
            office_mutation_duplication_query_response
        )

    def test_create_office_invalid_type(self):
        """
        Testing mutation to create an office with an invalid office type
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            office_mutation_query_invalid_type,
            office_mutation_query_invalid_type_response
        )
