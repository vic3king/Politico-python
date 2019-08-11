office_mutation_query = '''
mutation{
  createOffice(officeName: "presidente",
  ageLimit: 50, description: "my new office", officeType: "federal"){
    office{
      officeName
      ageLimit
      officeType
    }
  }
}
'''
office_mutation_query_invalid_type = '''
mutation{
  createOffice(officeName: "presidente", ageLimit: 50,
  description: "my new office", officeType: "federnal"){
    office{
      officeName
      ageLimit
      officeType
    }
  }
}
'''

office_mutation_duplication_query = '''
mutation{
  createOffice(officeName: "office", ageLimit: 50,
  description: "my new office", officeType: "federal"){
    office{
      officeName
      ageLimit
      officeType
    }
  }
}
'''
office_mutation_query_invalid_type_response = {
    "errors": [
        {
            "message": "Invalid type provided for field office_type",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createOffice"
            ]
        }
    ],
    "data": {
        "createOffice": None
    }
}
office_mutation_response = {
    "data": {
        "createOffice": {
            "office": {
                "officeName": "presidente",
                "ageLimit": "50",
                "officeType": "FEDERAL"
            }
        }
    }
}

office_mutation_duplication_query_response = {
    "errors": [
        {
            "message": "office Office name already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createOffice"
            ]
        }
    ],
    "data": {
        "createOffice": None
    }
}

allOffices_query = '''
{
  allOffices{
    officeName
    description
  }
}
'''
allOffices_query_response = {
    "data": {
        "allOffices": [
            {
                "officeName": "office",
                "description": "my testing office"
            }
        ]
    }
}

single_office_query = '''
{
  singleOffice(officeId: 1){
    office {
      officeName
      description
    }
  }
}
'''
single_office_query_response = {
    "data": {
        "singleOffice": {
            "office": {
                "officeName": "office",
                "description": "my testing office"
            }
        }
    }
}

single_office_query_not_found = '''
{
  singleOffice(officeId: 100){
    office {
      officeName
      description
    }
  }
}
'''


single_office_query_not_found_response = {
    "errors": [
        {
            "message": "office not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "singleOffice"
            ]
        }
    ],
    "data": {
        "singleOffice": None
    }
}
