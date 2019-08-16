from tests.base import (
    BaseTestCase,
    CommonTestCases
)

from fixtures.candidate.candidate_fixture import (
    create_candidate_mutatation,
    create_candidate_mutatation_response,
    response_when_candidate_exists,
    response_when_party_already_has_candidate
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateCandidate(BaseTestCase):

    def test_create_candidate_mutation(self):
        """
        Testing mutation to create a candidate to run for an opffice
        """

        # CommonTestCases.politician_token_assert_equal(
        #     self,
        #     create_candidate_mutatation,
        #     create_candidate_mutatation_response
        # )

    # def test_create_candidate_when_candidate_is_already_runnign(self):
    #     """
    #     Testing mutation to create a candidate a candidate when the candidate is already running for office
    #     """

    #     CommonTestCases.politician_token_assert_equal(
    #         self,
    #         create_candidate_mutatation,
    #         response_when_candidate_exists
    #     )

    # def test_create_candidate_when_party_has_candidate(self):
    #     """
    #     Testing mutation to create a candidate a candidate when the running party already has a candidate for that office
    #     """

    #     CommonTestCases.second_politician_token_assert_equal(
    #         self,
    #         create_candidate_mutatation,
    #         create_candidate_mutatation_response
    #     )
