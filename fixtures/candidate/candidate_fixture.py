create_candidate_mutatation = '''
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
create_candidate_mutatation_existing_party_diffrent_office = '''
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
create_candidate_mutatation_party_has_candidate = '''
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
                "userId": 1,
                "officeId": 1,
                "partyId": 1
            }
        }
    }
}
create_candidate_mutatation_existing_party_diffrent_office = {
    "data": {
        "createCandidate": {
            "candidate": {
                "userId": 2,
                "officeId": 2,
                "partyId": 1
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
                    "line": 2,
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
                    "line": 2,
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
