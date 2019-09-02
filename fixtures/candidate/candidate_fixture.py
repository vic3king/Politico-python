create_candidate_mutatation = '''
mutation{
  createCandidate(officeId: 1, partyId: 2){
    candidate{
      userId
      officeId
      partyId
    }
  }
}
'''
create_duplicat_candidate_mutatation = '''
mutation{
  createCandidate(officeId: 1, partyId: 1){
    candidate{
      userId
      officeId
      partyId
    }
  }
}
'''

create_candidate_mutatation_response = {
    "data": {
        "createCandidate": {
            "candidate": {
                "userId": 3,
                "officeId": 1,
                "partyId": 2
            }
        }
    }
}

response_when_party_already_has_candidate = {
    "errors": [
        {
            "message": "party already has a candidate",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createCandidate"
            ]
        }
    ],
    "data": {
        "createCandidate": None
    }
}

response_when_candidate_exists = {
    "errors": [
        {
            "message": "this candidate is already running for office",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createCandidate"
            ]
        }
    ],
    "data": {
        "createCandidate": None
    }
}
