login_user_query = '''
query{
  loginUser(userEmail:"admin@yahoo.com", userPassword:"12345678"){
    user {
      id
      firstName
      lastName
        email
    }
  }
}
'''

login_user_query_incorrect_credentials = '''
{
  loginUser(userEmail:"admin@yahoo.com", userPassword:"dfwefwe"){
    user {
        firstName
        lastName
        email
        userType
    }
  }
}
'''

login_user_query_user_not_found = '''
{
  loginUser(userEmail:"admffin@yahoo.com", userPassword:"dfwefwe"){
   user {
        firstName
        lastName
        email
        userType
    }
  }
}
'''
login_user_response = {
    "data": {
        "loginUser": {
            "user": {
                "id": "1",
                "firstName": "doe",
                "lastName": "jon",
                "email": "admin@yahoo.com"
            }
        }
    }
}

login_user_response_incorrect_credentials = {
    "errors": [
        {
            "message": "Incorrect credentials supplied",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "loginUser"
            ]
        }
    ],
    "data": {
        "loginUser": None
    }
}

login_user_response_user_not_found = {
    "errors": [
        {
            "message": "User not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "loginUser"
            ]
        }
    ],
    "data": {
        "loginUser": None
    }
}
