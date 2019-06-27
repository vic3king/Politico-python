null = None

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
