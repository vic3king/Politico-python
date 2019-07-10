null = None
all_users_query = '''
query{
  allUsers {
    firstName
    lastName
    userType
  }
}
'''

all_users_response = {
    "data": {
        "allUsers": [
            {
                "firstName": "doe",
                "lastName": "jon",
                "userType": "ADMIN"
            },
            {
                "firstName": "doe",
                "lastName": "jon",
                "userType": "CITIZEN"
            },
            {
                "firstName": "doe",
                "lastName": "jon",
                "userType": "POLITICIAN"
            }
        ]
    }
}


user_mutation_query = '''
mutation {
  createUser(firstName: "doe", lastName: "jon", otherNames: "smith", email: "example@yahoo.com", password: "12345678", picture: "https://picsum.photos/200", userType: "admin") { # noqa
    user {
      firstName
      lastName
      otherNames
      email
      picture
      userType
    }
  }
}

'''
user_mutation_query_invalid_email = '''
mutation {
  createUser(firstName: "doe", lastName: "jon", otherNames: "smith", email: "exampleyahoo.com", password: "12345678", picture: "https://picsum.photos/200", userType: "admin") { # noqa
    user {
      firstName
      lastName
      otherNames
      email
      picture
      userType
    }
  }
}

'''

user_mutation_response = {
    "data": {
        "createUser": {
            "user": {
                "firstName": "doe",
                "lastName": "jon",
                "otherNames": "smith",
                "email": "example@yahoo.com",
                "picture": "https://picsum.photos/200",
                "userType": "ADMIN"
            }
        }
    }
}

user_mutation_response_invalid_email = {
    "errors": [
        {
            "message": "This email is not allowed",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createUser"
            ]
        }
    ],
    "data": {
        "createUser": null
    }
}

user_duplication_mutation_response = {
    "errors": [
        {
            "message": "example@yahoo.com User email already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createUser"
            ]
        }
    ],
    "data": {
        "createUser": null
    }
}
