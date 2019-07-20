party_mutation_query = '''
mutation{
  createParty(partyName: "test-party",
  hqAddress: "no 5 city of power avenue", logoUrl: "www.ipsum/pic"){
    party{
      partyName
      logoUrl
      status
      hqAddress
      id
    }
  }
}
'''

party_mutation_duplication_query = '''
mutation{
  createParty(partyName: "party",
  hqAddress: "no 5 city of power avenue", logoUrl: "www.ipsum/pic"){
    party{
      partyName
      logoUrl
      status
      hqAddress
      id
    }
  }
}
'''
party_invalid_address_mutation_query = '''
mutation{
  createParty(partyName: "party",
  hqAddress: "no 5 city of asdf avenue", logoUrl: "www.ipsum/pic"){
    party{
      partyName
      logoUrl
      status
      hqAddress
      id
    }
  }
}
'''

party_mutation_response = {
    "data": {
        "createParty": {
            "party": {
                "partyName": "test-party",
                "logoUrl": "www.ipsum/pic",
                "status": "NEW",
                "hqAddress": "5 City Of Power Avenue, Somolu, Lagos, Nigeria",
                "id": "2"
            }
        }
    }
}

party_mutation_duplication_response = {
    "errors": [
        {
            "message": "party Party name already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createParty"
            ]
        }
    ],
    "data": {
        "createParty": None
    }
}

party_mutation_invalid_address_response = {
    "errors": [
        {
            "message": "no 5 city of asdf avenue not found, enter a valid address",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createParty"
            ]
        }
    ],
    "data": {
        "createParty": None
    }
}
