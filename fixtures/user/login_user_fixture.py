login_user_query = '''
query{
    loginUser(userEmail: "admin@yahoo.com", userPassword: "12345678"){
            firstName
            lastName
            email
            userType
      }
    }
'''

login_user_query_incorrect_credentials = '''
{
  loginUser(userEmail:"admin@yahoo.com", userPassword:"dfwefwe"){
    firstName
    lastName
    email
    userType
  }
}
'''

login_user_query_user_not_found = '''
{
  loginUser(userEmail:"admffin@yahoo.com", userPassword:"dfwefwe"){
    firstName
    lastName
    email
    userType
  }
}
'''
login_user_response = {
    "data": {
        "loginUser": {
            "firstName": "doe",
            "lastName": "jon",
            "email": "admin@yahoo.com",
            "userType": "ADMIN"
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
