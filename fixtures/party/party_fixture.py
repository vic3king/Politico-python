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
delete_party_mutation = '''
mutation{
  deleteParty(partyId: 1){
    message
  }
}
'''

delete_party_does_not_exist_mutation = '''
mutation{
  deleteParty(partyId: 40){
    message
  }
}
'''

delete_party_mutation_response = {
    "data": {
        "deleteParty": {
            "message": "party party was deleted successfully"
        }
    }
}
delete_party_does_not_exist_response = {
    "errors": [
        {
            "message": "Party does not exist",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "deleteParty"
            ]
        }
    ],
    "data": {
        "deleteParty": None
    }
}

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

allParties_query = '''
 {
  allParties{
    partyName
    hqAddress
    logoUrl
  }
}
 '''
allParties_query_response = {
    "data": {
        "allParties": [
            {
                "partyName": "party",
                "hqAddress": "5 City Of Power Avenue, Somolu, Lagos, Nigeria",
                "logoUrl": "www.ipsum/pic"
            }
        ]
    }
}

single_party_query = '''
{
  singleParty(partyId: 1){
    party{
      partyName
      hqAddress
      logoUrl
    }
  }
}
'''
single_party_query_response = {
    "data": {
        "singleParty": {
            "party": {
                "partyName": "party",
                "hqAddress": "5 City Of Power Avenue, Somolu, Lagos, Nigeria",
                "logoUrl": "www.ipsum/pic"
            }
        }
    }
}

single_party_query_not_found = '''
{
  singleParty(partyId: 30){
    party{
      partyName
      hqAddress
      logoUrl
    }
  }
}
'''

single_party_query_not_found_response = {
    "errors": [
        {
            "message": "party not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "singleParty"
            ]
        }
    ],
    "data": {
        "singleParty": None
    }
}
