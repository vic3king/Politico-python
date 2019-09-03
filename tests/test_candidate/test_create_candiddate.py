# from tests.base import (
#     BaseTestCase,
#     CommonTestCases
# )

# from fixtures.candidate.candidate_fixture import (
#     create_candidate_mutatation,
#     create_candidate_mutatation_response,
#     response_when_candidate_exists,
#     response_when_party_already_has_candidate,
#     create_duplicat_candidate_mutatation
# )

# import sys
# import os
# sys.path.append(os.getcwd())


# class TestCreateCandidate(BaseTestCase):

#     def test_create_candidate_mutation(self):
#         """
#         Testing mutation to create a candidate to run for an office
#         """

#         CommonTestCases.politician_token_assert_equal(
#             self,
#             create_candidate_mutatation,
#             create_candidate_mutatation_response
#         )

#     def test_create_candidate_when_candidate_is_already_running(self):
#         """
#         Testing mutation to create a candidate a candidate when the candidate is already running for office
#         """

#         CommonTestCases.dup_politician_token_assert_equal(
#             self,
#             create_duplicat_candidate_mutatation,
#             response_when_candidate_exists
#         )

#     def test_create_candidate_when_party_has_candidate(self):
#         """
#         Testing mutation to create a candidate when the running party already has a candidate for that office
#         """

#         CommonTestCases.politician_token_assert_equal(
#             self,
#             create_duplicat_candidate_mutatation,
#             response_when_party_already_has_candidate,
#         )
