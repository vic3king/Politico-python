import graphene
from graphene_sqlalchemy import (SQLAlchemyObjectType)

from api.user.models import User as UserModel
# from utilities.validators import verify_email


class User(SQLAlchemyObjectType):
    """
        Autogenerated return type of a user
    """
    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):
    """
        Mutation to create a user
    """
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        other_names = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        picture = graphene.String()
        user_type = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user = UserModel(**kwargs)
        # if verify_email(user.email):
        #     raise GraphQLError("This email is not allowed")
        user.save()
        return CreateUser(user=user)


class allUsers(graphene.ObjectType):
    """
        all users
    """
    users = graphene.List(User)


class Query(graphene.ObjectType):
    all_users = graphene.List(
        User,
        description="Returns a list of all users")

    def resolve_all_users(self, info):
        # get all users
        query = User.get_query(info)
        return query


class Mutation(graphene.ObjectType):
    """
        Mutation to create user
    """
    create_user = CreateUser.Field(
        description="Creates a new user with the arguments\
            \n- first_name: The first_name field of the user[required]\
            \n- last_name: The last_name field of the user[required]\
            \n- other_names: The other_names field of the user\
            \n- email: The email field of the user[required]\
            \n- password: The password field of the user[required]\
            \n- user_type: The type field of a user[required]\
            \n- picture: The picture field of a user")
